# 2. Python 설치하기

!!! abstract "이 페이지에서 하는 일"
    - 데이터 처리·분석에 쓰는 **Python**을 설치합니다
    - 터미널에서 `python --version`이 숫자를 답하면 통과입니다

- **파이썬(Python)**은 데이터 처리, 분석, AI 서버 구축에 강점이 있는 언어입니다.
- 실습에서는 AI가 엑셀·PDF 자료를 읽고 정리할 때 **뒤에서 조용히** 이걸 씁니다. 여러분이 직접 다룰 일은 없습니다.


## 다운로드와 설치

Python 공식 사이트에서 최신 버전(3.10 이상)을 받습니다.

```
https://www.python.org/downloads/
```

**1단계.** 페이지를 아래로 내려 **Active Python releases** 표에서 설치할 버전의 `Download`를 누릅니다.

![python.org 다운로드 페이지의 Active Python releases 표 — 설치할 버전의 Download 링크](../../images/setup/python_add_to_path.png)

**2단계.** 열린 페이지 맨 아래 **Files** 표에서 받을 파일을 고릅니다.

- **Windows** → `Windows installer (64-bit)` (**Recommended** 표시가 붙어 있습니다)
- **macOS** → `macOS installer` (`.pkg` 파일을 실행해 안내대로 설치합니다)

![Files 표에서 Windows installer (64-bit) Recommended 항목 선택](../../images/setup/python_install_1.png)

**3단계.** 받은 설치 파일을 실행합니다.

!!! danger "Windows에서는 이 체크박스가 가장 중요합니다"
    설치 **첫 화면 아래쪽**의 **`Add python.exe to PATH`** 체크박스를 **반드시 켜세요.** 이걸 놓치면 뒤에서 `python` 명령이 동작하지 않습니다.

    이미 안 켜고 설치했다면, 설치 파일을 다시 실행해 `Modify`로 고칠 수 있습니다.

![Python 설치 첫 화면 — 아래쪽 Add python.exe to PATH(`PATH에 추가`) 체크박스가 켜져 있는 상태](../../images/setup/python_install_2.png)

체크한 뒤 `Install Now`를 눌러 설치를 완료합니다.

## 설치 확인

설치가 끝나면 **새 명령 프롬프트 창**을 열고(윈도우 키 → `cmd` 입력 → Enter, 맥은 Spotlight에서 '터미널' 검색) 아래를 입력합니다.

```bash
python --version
```

!!! success "이렇게 나오면 정상입니다"
    `Python 3.10` 이상 숫자가 출력됩니다. (macOS에서는 `python3 --version`으로 확인하세요.)

!!! warning "이렇게 나왔다면"
    - `python`을 쳤더니 **Microsoft Store가 열린다** → `Add Python to PATH`를 켜지 않고 설치한 경우입니다. 설치 파일을 다시 실행해 고치세요.
    - `명령을 찾을 수 없습니다` / `command not found` → 창을 완전히 닫았다가 **새 창**에서 다시 시도하세요. 그래도 같으면 재설치가 필요합니다.

<div class="stage-nav" markdown>
**← 이전** [① VS Code 설치](vscode.md) · **다음 →** [③ Node.js 설치](nodejs.md)
</div>
