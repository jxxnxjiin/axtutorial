#!/usr/bin/env python3
"""ax-tutor 위키 빌더 — ax-wiki의 md를 Claude Code 톤 정적 HTML로 렌더링한다.
   실행: python3 build_wiki.py   (../ax-wiki/docs 를 읽어 이 레포에 페이지 생성)
"""
import os, re, html as _html
import markdown
from pymdownx.slugs import slugify

SRC = os.path.join(os.path.dirname(__file__), '..', 'ax-wiki', 'docs')
OUT = os.path.dirname(__file__)

# 사이드바 = 모든 페이지 공통. (섹션제목, [(짧은라벨, md경로)]) — mkdocs.yml nav를 옮김.
NAV = [
    ('시작하기', [
        ('0 · 준비물과 사전 설치', 'start/prepare.md'),
        ('1 · 처음 5분', 'start/first-5min.md'),
        ('2 · 오후 규칙 3가지', 'start/rules.md'),
    ]),
    ('실습 1 · 물류비 마감', [
        ('개요', 'lab1/index.md'),
        ('1 · 요금표를 표로', 'lab1/step1.md'),
        ('2 · 청구서 합치기', 'lab1/step2.md'),
        ('3 · 120건 재계산', 'lab1/step3.md'),
        ('4 · 검증 설계·검산', 'lab1/step4.md'),
        ('＋ 더 해보기', 'lab1/extra.md'),
    ]),
    ('실습 2 · 계약·입찰 레이더', [
        ('개요', 'lab2/index.md'),
        ('1 · 계약서 한 장', 'lab2/step1.md'),
        ('2 · 열두 건으로', 'lab2/step2.md'),
        ('3 · 회사소개 문단', 'lab2/step3.md'),
        ('4 · 공고 가져와 나누기', 'lab2/step4.md'),
        ('5 · 설명서 남기기', 'lab2/step5.md'),
        ('＋ 영문·스캔 PDF', 'lab2/extra.md'),
    ]),
    ('실습 3 · 근거 붙인 보고문', [
        ('개요', 'lab3/index.md'),
        ('1 · 일단 써보게', 'lab3/step1.md'),
        ('2 · 숫자마다 출처', 'lab3/step2.md'),
        ('3 · 숫자 5개 역추적', 'lab3/step3.md'),
        ('4·5 · 없는 문장·톤 두 벌', 'lab3/step4.md'),
        ('＋ 더 해보기', 'lab3/extra.md'),
    ]),
    ('실습 4 · 대시보드와 디자인', [
        ('개요', 'lab4/index.md'),
        ('1 · 무엇을 보여줄지', 'lab4/step1.md'),
        ('2 · 뼈대·검산', 'lab4/step2.md'),
        ('3 · Before 캡처', 'lab4/step3.md'),
        ('4 · 말로 인상 바꾸기', 'lab4/step4.md'),
        ('5 · 두 무드 비교', 'lab4/step5.md'),
        ('6 · 다크모드·반응형', 'lab4/step6.md'),
        ('7 · 재검산·After', 'lab4/step7.md'),
        ('막혔을 때 쓰는 문장', 'lab4/stuck.md'),
    ]),
    ('여유 실습', [
        ('A · 회의 녹취 정리', 'lab5/index.md'),
        ('A-1 · 결정만 골라내기', 'lab5/step1.md'),
        ('A-2 · 담당자·마감', 'lab5/step2.md'),
        ('A-3 · 근거 남기기', 'lab5/step3.md'),
        ('B · 링크로 공유', 'lab6/index.md'),
    ]),
    ('도움말', [
        ('에러가 났어요', 'help/errors.md'),
        ('이 말이 무슨 뜻이죠', 'help/glossary.md'),
        ('AI에게 잘 시키는 법', 'help/how-to-ask.md'),
        ('오늘 내가 친 문장', 'help/prompts.md'),
        ('강의 끝나고 뭘 해볼까', 'help/next.md'),
    ]),
]

# 이전/다음용 평탄 목록 (섹션명도 함께)
FLAT = [(lbl, path, sec) for sec, items in NAV for lbl, path in items]

ICONS = {':material-run-fast:': '🏃', ':material-account-group:': '👥'}

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

def sidebar(cur, prefix='../', home='remote'):
    # home='local'  : 홈(index.html) 자신 → 페이지 내 앵커로 링크
    # home='remote' : 하위 페이지 → 홈으로 돌아가는 링크
    if home == 'local':
        rows = ['<div class="nav-h">// 홈</div>',
                '<a class="nav-a" href="#overview"><span class="g">◆</span> 오늘의 지도</a>',
                '<a class="nav-a" href="#timetable"><span class="g">◷</span> 시간표</a>',
                '<a class="nav-a" href="#materials"><span class="g">▤</span> 강의 자료 내려받기</a>']
    else:
        rows = ['<div class="nav-h">// 홈</div>',
                f'<a class="nav-a" href="{prefix}index.html"><span class="g">◆</span> 오늘의 지도</a>',
                f'<a class="nav-a" href="{prefix}index.html#materials"><span class="g">▤</span> 강의 자료 내려받기</a>']
    for sec, items in NAV:
        rows.append(f'<div class="nav-h">// {sec}</div><div class="tree">')
        if sec == '시작하기':
            ta = ' active' if cur == 'types/index.md' else ''
            rows.append(f'<a class="nav-a{ta}" href="{prefix}types/index.html"><span class="g">◆</span> 여섯 가지 업무 유형</a>')
        for lbl, path in items:
            active = ' active' if path == cur else ''
            rows.append(f'<a class="nav-a{active}" href="{prefix}{path[:-3]}.html">{_html.escape(lbl)}</a>')
        rows.append('</div>')
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
    parts = ['<nav class="pager">']
    if idx == 0:
        prev = ('오늘의 지도', '../index.html')
    else:
        l, p, _ = FLAT[idx-1]; prev = (l, f'../{p[:-3]}.html')
    parts.append(f'<a class="prev" href="{prev[1]}"><span class="lbl">← 이전</span><span class="ttl">{_html.escape(prev[0])}</span></a>')
    if idx < len(FLAT)-1:
        l, p, _ = FLAT[idx+1]
        parts.append(f'<a class="next" href="../{p[:-3]}.html"><span class="lbl">다음 →</span><span class="ttl">{_html.escape(l)}</span></a>')
    parts.append('</nav>')
    return '\n'.join(parts)

TEMPLATE = '''<!doctype html>
<html lang="ko" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%%TITLE%% · ax-tutor</title>
<meta name="description" content="%%DESC%%">
<link rel="stylesheet" href="../assets/site.css">
</head>
<body>
<div class="shell">
  <aside class="side" id="side">
    <div class="brand">
      <a class="brand__row" href="../index.html" style="text-decoration:none">
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
      <a class="iconbtn" href="../index.html" title="홈">↖ home</a>
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
<script src="../assets/site.js"></script>
</body>
</html>
'''

# 빌드 대상이 아닌 손수 만든 정적 페이지들 — nav 블록만 NAV에서 다시 주입해 동기화.
# (relpath, sidebar 인자) — 이 목록만 관리하면 홈/유형 페이지 nav도 단일 원본을 따른다.
STATIC_NAV = [
    ('index.html',       dict(cur=None,             prefix='',   home='local')),
    ('types/index.html', dict(cur='types/index.md', prefix='../', home='remote')),
]

def inject_nav():
    for relpath, kw in STATIC_NAV:
        fp = os.path.join(OUT, relpath)
        with open(fp, encoding='utf-8') as f:
            page = f.read()
        nav = sidebar(**kw)
        new, cnt = re.subn(r'<nav>.*?</nav>', lambda m: f'<nav>\n{nav}\n</nav>',
                           page, count=1, flags=re.S)
        if cnt == 0:
            raise SystemExit(f'✗ {relpath}: <nav>…</nav> 블록을 찾지 못함 — 수동 확인 필요')
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(new)
        print(f'  ↳ nav 동기화: {relpath}')

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
        # 제목 = 첫 h1 텍스트
        m = re.search(r'<h1[^>]*>(.*?)(<a class="headerlink".*?</a>)?</h1>', body, re.S)
        title = re.sub('<[^>]+>', '', m.group(1)).strip() if m else lbl
        page = (TEMPLATE
                .replace('%%TITLE%%', _html.escape(title))
                .replace('%%DESC%%', _html.escape(f'{sec} — {title} · ax-tutor 실습 위키'))
                .replace('%%SIDEBAR%%', sidebar(path))
                .replace('%%PATH%%', _html.escape(path))
                .replace('%%SECTION%%', _html.escape(sec))
                .replace('%%CONTENT%%', body)
                .replace('%%PAGER%%', pager(idx))
                .replace('%%TOC%%', toc_html(md.toc_tokens)))
        dst = os.path.join(OUT, path[:-3] + '.html')
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'w', encoding='utf-8') as f:
            f.write(page)
        n += 1
    print(f'✓ {n} pages generated')
    inject_nav()

if __name__ == '__main__':
    build()
