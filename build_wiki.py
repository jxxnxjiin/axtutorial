#!/usr/bin/env python3
"""ax-tutor 위키 빌더 — ax-wiki의 md를 Claude Code 톤 정적 HTML로 렌더링한다.
   실행: python3 build_wiki.py   (../ax-wiki/docs 를 읽어 이 레포에 페이지 생성)
"""
import os, re, html as _html
import markdown
import yaml
from pymdownx.slugs import slugify

SRC = os.path.join(os.path.dirname(__file__), 'docs')
OUT = os.path.dirname(__file__)

# 사이드바 구조 = 단일 소스 nav.yml. (스키마 설명은 nav.yml 주석 참고)
with open(os.path.join(os.path.dirname(__file__), 'nav.yml'), encoding='utf-8') as _f:
    NAV_TREE = yaml.safe_load(_f)['nav']

def rel_prefix(path):
    # 출력 HTML 위치의 깊이만큼 '../' — 자산/링크 상대경로를 자동 계산(폴더 중첩 허용).
    return '../' * path.count('/')

def _flatten(nodes, section=None):
    # 트리를 (라벨, 경로, 최상위섹션) 리프 목록으로. group 은 최상위 섹션명만 물려준다.
    out = []
    for node in nodes:
        if 'group' in node:
            out += _flatten(node['children'], section or node['group'])
        else:
            out.append((node['label'], node['path'], section))
    return out

# 이전/다음·빌드 대상 = md 가 실제로 있는 리프만. (types/index.md 처럼 소스 없는 정적 링크는 제외)
FLAT = [(l, p, s) for l, p, s in _flatten(NAV_TREE) if os.path.exists(os.path.join(SRC, p))]

ICONS = {':material-run-fast:': '🏃', ':material-account-group:': '👥'}

# 제목 슬러그(=본문 h1·목차 앵커 id) 생성기 — md 목차와 동일 규칙.
SLUG = slugify(case='lower')

def md_engine():
    return markdown.Markdown(extensions=[
        'admonition', 'pymdownx.details', 'pymdownx.superfences', 'pymdownx.tabbed',
        'pymdownx.highlight', 'pymdownx.inlinehilite', 'pymdownx.caret', 'pymdownx.keys',
        'pymdownx.mark', 'pymdownx.tilde', 'pymdownx.critic',
        'attr_list', 'md_in_html', 'tables', 'def_list', 'pymdownx.tasklist', 'toc',
    ], extension_configs={
        'pymdownx.tabbed': {'alternate_style': True},
        'pymdownx.tasklist': {'custom_checkbox': True},
        'toc': {'permalink': True, 'slugify': slugify(case='lower')},
    })

def preprocess(text):
    for k, v in ICONS.items():
        text = text.replace(k, v)
    text = re.sub(r':[a-z]+-[a-z0-9-]+:', '', text)   # 남은 아이콘 토큰 제거
    return text

def rewrite_links(h):
    # 내부 .md 링크 → .html (외부 http 링크는 건드리지 않음)
    def repl(m):
        pre, path, anchor = m.group(1), m.group(2), m.group(3) or ''
        if path.startswith('http'):
            return m.group(0)
        return f'{pre}="{path}.html{anchor}"'
    return re.sub(r'(href|src)="(?!https?:)([^"#]+)\.md(#[^"]*)?"', repl, h)

def _render_nodes(nodes, cur, prefix):
    # nav 트리를 사이드바 HTML 행들로. group → 헤더+.tree(중첩 시 CSS가 자동 들여쓰기).
    rows = []
    for node in nodes:
        if 'group' in node:
            rows.append(f'<div class="nav-h">// {node["group"]}</div><div class="tree">')
            rows += _render_nodes(node['children'], cur, prefix)
            rows.append('</div>')
        else:
            active = ' active' if node['path'] == cur else ''
            icon = f'<span class="g">{node["icon"]}</span> ' if node.get('icon') else ''
            href = f'{prefix}{node["path"][:-3]}.html'
            rows.append(f'<a class="nav-a{active}" href="{href}">{icon}{_html.escape(node["label"])}</a>')
    return rows

def sidebar(cur, prefix='../', home='remote', home_rows=None):
    # home='local'  : 홈(index.html) 자신 → 페이지 내 섹션 앵커로 링크(섹션의 data-nav 속성에서 생성)
    # home='remote' : 하위 페이지 → 홈으로 돌아가는 링크
    if home == 'local':
        rows = list(home_rows) if home_rows else ['<div class="nav-h">// 홈</div>']
    else:
        rows = ['<div class="nav-h">// 홈</div>',
                f'<a class="nav-a" href="{prefix}index.html#materials"><span class="g">▤</span> 강의 자료 내려받기</a>']
    rows += _render_nodes(NAV_TREE, cur, prefix)
    return '\n'.join(rows)

def toc_html(tokens):
    def walk(items):
        out = []
        for t in items:
            if t['level'] > 3:
                continue
            cls = ' class="t3"' if t['level'] == 3 else ''
            out.append(f'<a href="#{t["id"]}"{cls}>{_html.escape(t["name"])}</a>')
            out += walk(t.get('children', []))
        return out
    links = walk(tokens)
    if not links:
        return ''
    return '<h4>On this page</h4>\n' + '\n'.join(links)

def pager(idx):
    pfx = rel_prefix(FLAT[idx][1])   # 현재 페이지 깊이 기준 상대경로
    parts = ['<nav class="pager">']
    if idx == 0:
        prev = ('시간표', f'{pfx}index.html')
    else:
        l, p, _ = FLAT[idx-1]; prev = (l, f'{pfx}{p[:-3]}.html')
    parts.append(f'<a class="prev" href="{prev[1]}"><span class="lbl">← 이전</span><span class="ttl">{_html.escape(prev[0])}</span></a>')
    if idx < len(FLAT)-1:
        l, p, _ = FLAT[idx+1]
        parts.append(f'<a class="next" href="{pfx}{p[:-3]}.html"><span class="lbl">다음 →</span><span class="ttl">{_html.escape(l)}</span></a>')
    parts.append('</nav>')
    return '\n'.join(parts)

TEMPLATE = '''<!doctype html>
<html lang="ko" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%%TITLE%% · ax-tutor</title>
<meta name="description" content="%%DESC%%">
<link rel="stylesheet" href="%%PREFIX%%assets/site.css">
</head>
<body>
<div class="shell">
  <aside class="side" id="side">
    <div class="brand">
      <a class="brand__row" href="%%PREFIX%%index.html" style="text-decoration:none">
        <span class="ast mono">✻</span>
        <div><div class="brand__name">ax<b>-</b>tutor</div></div>
      </a>
      <div class="brand__sub">Claude Code · 실습 위키</div>
      <div class="session"><span class="dot"></span><span class="live">LIVE</span>
        <span style="color:var(--muted)">강의 진행 중</span><span class="clock mono" id="clock">--:--</span></div>
    </div>
    <nav>%%SIDEBAR%%</nav>
    <div class="side__foot">
      <button class="iconbtn" id="themeBtn" title="테마 전환"><span id="themeIc">◐</span> <span id="themeLbl">light</span></button>
      <a class="iconbtn" href="%%PREFIX%%index.html" title="홈">↖ home</a>
    </div>
  </aside>
  <main class="main">
    <div class="cmdbar mono">
      <button class="burger" id="burger" aria-label="메뉴">≡</button>
      <span class="path"><b>~/ax-tutor</b> <span class="full">$ cat</span> <span class="cur">%%PATH%%</span></span>
      <span class="caret"></span><span class="spacer"></span>
      <span class="stat">%%SECTION%%</span>
    </div>
    <div class="wrap">
      <article class="doc md rise">
        <div class="kicker mono"><b>//</b> %%SECTION%%</div>
%%CONTENT%%
%%PAGER%%
      </article>
      <aside class="toc mono">%%TOC%%</aside>
    </div>
  </main>
</div>
<script src="%%PREFIX%%assets/site.js"></script>
</body>
</html>
'''

# 빌드 대상이 아닌 손수 만든 정적 페이지들 — nav 블록만 NAV에서 다시 주입해 동기화.
# (relpath, sidebar 인자) — 이 목록만 관리하면 홈/유형 페이지 nav도 단일 원본을 따른다.
STATIC_NAV = [
    ('index.html',       dict(cur=None,             prefix='',   home='local')),
    ('types/index.html', dict(cur='types/index.md', prefix='../', home='remote')),
]

# 정적 홈/유형 페이지의 좌측 홈 nav·우측 On this page 는 페이지 안 섹션이 스스로 들고 있는
# data-nav / data-toc 속성에서 생성한다. 앵커 id 와 라벨이 같은 요소에 붙어 있어
# '섹션은 지웠는데 목차만 남는' desync 가 원천 차단된다.
#   data-nav="라벨"        : 좌측 홈 nav 에 노출 (data-nav-icon="◆" 로 앞 기호 지정)
#   data-toc="라벨"        : 우측 On this page 에 노출
_TAG_RE  = re.compile(r'<(?:section|h[1-6])\b([^>]*)>')
_ATTR_RE = re.compile(r'([a-zA-Z][\w-]*)="([^"]*)"')

def _anchored(page, key):
    # id 와 key 속성을 함께 가진 태그를 문서 순서대로 [attrs dict] 로 수집.
    out = []
    for m in _TAG_RE.finditer(page):
        a = dict(_ATTR_RE.findall(m.group(1)))
        if 'id' in a and key in a:
            out.append(a)
    return out

def home_nav_rows(page):
    rows = ['<div class="nav-h">// 홈</div>']
    for a in _anchored(page, 'data-nav'):
        icon = f'<span class="g">{a["data-nav-icon"]}</span> ' if a.get('data-nav-icon') else ''
        rows.append(f'<a class="nav-a" href="#{a["id"]}">{icon}{_html.escape(a["data-nav"])}</a>')
    return rows

def toc_block(page):
    rows = ['<h4>On this page</h4>']
    for a in _anchored(page, 'data-toc'):
        rows.append(f'<a href="#{a["id"]}">{_html.escape(a["data-toc"])}</a>')
    return '\n'.join(rows)

def inject_nav():
    for relpath, kw in STATIC_NAV:
        fp = os.path.join(OUT, relpath)
        with open(fp, encoding='utf-8') as f:
            page = f.read()
        home_rows = home_nav_rows(page) if kw.get('home') == 'local' else None
        nav = sidebar(cur=kw['cur'], prefix=kw['prefix'], home=kw['home'], home_rows=home_rows)
        page, cnt = re.subn(r'<nav>.*?</nav>', lambda m: f'<nav>\n{nav}\n</nav>',
                            page, count=1, flags=re.S)
        if cnt == 0:
            raise SystemExit(f'✗ {relpath}: <nav>…</nav> 블록을 찾지 못함 — 수동 확인 필요')
        toc = toc_block(page)
        page, tcnt = re.subn(r'(<aside class="toc[^"]*">).*?(</aside>)',
                             lambda m: f'{m.group(1)}\n{toc}\n      {m.group(2)}',
                             page, count=1, flags=re.S)
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(page)
        print(f'  ↳ nav{"·toc" if tcnt else ""} 동기화: {relpath}')

def build():
    n = 0
    for idx, (lbl, path, sec) in enumerate(FLAT):
        src = os.path.join(SRC, path)
        with open(src, encoding='utf-8') as f:
            raw = f.read()
        md = md_engine()
        body = md.convert(preprocess(raw))
        body = rewrite_links(body)
        # md 본문 끝의 손수 적은 이전/다음 블록 제거 — 아래 생성 .pager로 대체
        body = re.sub(r'<div class="stage-nav">.*?</div>\s*', '', body, flags=re.S)
        # 제목 = nav.yml label 로 통일. md 의 첫 # 은 무시(제거)하고 label 로 h1 주입.
        # (본문 h1·우측 목차 첫 항목·<title> 세 곳이 label 로 일치 → 제목 desync 방지)
        title = lbl
        slug = SLUG(title, '-')
        body = re.sub(r'<h1\b[^>]*>.*?</h1>\s*', '', body, count=1, flags=re.S)
        body = (f'<h1 id="{slug}">{_html.escape(title)}'
                f'<a class="headerlink" href="#{slug}" title="Permanent link">&para;</a></h1>\n'
                + body)
        toks = md.toc_tokens
        if toks and toks[0].get('level') == 1:
            toks = [{**toks[0], 'name': title, 'id': slug}] + list(toks[1:])
        else:
            toks = [{'level': 1, 'id': slug, 'name': title, 'children': []}] + list(toks)
        pfx = rel_prefix(path)
        page = (TEMPLATE
                .replace('%%TITLE%%', _html.escape(title))
                .replace('%%DESC%%', _html.escape(f'{sec} — {title} · ax-tutor 실습 위키'))
                .replace('%%SIDEBAR%%', sidebar(path, pfx))
                .replace('%%PATH%%', _html.escape(path))
                .replace('%%SECTION%%', _html.escape(sec))
                .replace('%%CONTENT%%', body)
                .replace('%%PAGER%%', pager(idx))
                .replace('%%TOC%%', toc_html(toks))
                .replace('%%PREFIX%%', pfx))
        dst = os.path.join(OUT, path[:-3] + '.html')
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(page)
        n += 1
    print(f'✓ {n} pages generated')
    inject_nav()

def prune():
    # 더 이상 md와 연결되지 않는 .html 삭제.
    # keep = FLAT(빌드 산출물) ∪ STATIC_NAV(손수 만든 정적 페이지). 그 외 .html은 stale로 간주.
    # 섹션을 통째로 NAV에서 빼도(lab5/lab6 등) 걸리도록 OUT 전체를 스캔하되,
    # 콘텐츠가 아닌 자원 폴더(assets/images/materials)는 건너뛴다.
    keep  = {os.path.normpath(os.path.join(OUT, p[:-3] + '.html')) for _, p, _ in FLAT}
    keep |= {os.path.normpath(os.path.join(OUT, rel)) for rel, _ in STATIC_NAV}
    SKIP = {'__pycache__', 'assets', 'images', 'materials', '.git'}
    removed = 0
    for root, dirs, files in os.walk(OUT):
        dirs[:] = [d for d in dirs if d not in SKIP]
        for name in files:
            if not name.endswith('.html'):
                continue
            fp = os.path.normpath(os.path.join(root, name))
            if fp not in keep:
                os.remove(fp)
                print(f'  ✗ 삭제(연결 끊긴 HTML): {os.path.relpath(fp, OUT)}')
                removed += 1
    # 삭제로 비게 된 폴더 정리 (자원 폴더·루트는 제외)
    for root, _, _ in os.walk(OUT, topdown=False):
        rel = os.path.relpath(root, OUT)
        if rel == '.' or set(rel.split(os.sep)) & SKIP:
            continue
        if not os.listdir(root):
            os.rmdir(root)
            print(f'  ✗ 빈 폴더 삭제: {rel}')
    print(f'✓ {removed} stale page(s) removed' if removed else '✓ stale 페이지 없음')

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser(description='ax-tutor 위키 빌더')
    ap.add_argument('--prune', action='store_true',
                    help='빌드 후 FLAT(NAV)에 없는 연결 끊긴 .html 페이지를 삭제')
    args = ap.parse_args()
    build()
    if args.prune:
        prune()
