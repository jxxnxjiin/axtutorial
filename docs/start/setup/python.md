# 2. Python 설치하기

!!! abstract "이 페이지에서 하는 일"
    - 데이터 처리·분석에 쓰는 **Python**을 설치합니다
    - 터미널에서 `python --version` 이 숫자를 답하면 통과입니다

- **파이썬(Python)**은 데이터 처리, 분석, AI 서버 구축에 강점이 있는 언어입니다.
- 실습에서는 PDF나 이미지를 **전처리·분석**하고, 데이터를 **취합·정리**하는 데 씁니다.

---

## 다운로드와 설치

Python 공식 사이트에서 최신 버전(3.10 이상)을 받습니다.

```
https://www.python.org/downloads/
```

- **Windows** → 노란 `Download Python 3.x.x` 버튼으로 설치 파일을 받아 실행합니다.
- **macOS** → 같은 버튼으로 받은 `.pkg` 파일을 실행해 안내대로 설치합니다.

!!! danger "Windows에서는 이 체크박스가 가장 중요합니다"
    설치 **첫 화면 아래쪽**의 **`Add Python to PATH`** 체크박스를 **반드시 켜세요.** 이걸 놓치면 뒤에서 `python` 명령이 동작하지 않습니다.

    이미 안 켜고 설치했다면, 설치 파일을 다시 실행해`Modify`로 고칠 수 있습니다.

체크한 뒤 `Install Now`를 눌러 설치를 완료합니다.

---

## 설치 확인

설치가 끝나면 **새 명령 프롬프트(또는 터미널) 창**을 열고 아래를 입력합니다.

```bash
python --version
```

!!! success "이렇게 나오면 정상입니다"
    `Python 3.10` 이상 숫자가 출력됩니다. (macOS에서는 `python3 --version` 으로 확인하세요.)

!!! warning "이렇게 나왔다면"
    - `python`을 쳤더니 **Microsoft Store가 열린다** → `Add Python to PATH`를 켜지 않고 설치한 경우입니다. 설치 파일을 다시 실행해 고치세요.
    - `명령을 찾을 수 없습니다` / `command not found` → 창을 완전히 닫았다가 **새 창**에서 다시 시도하세요. 그래도 같으면 재설치가 필요합니다.

<div class="stage-nav" markdown>
**← 이전** [① VS Code 설치](vscode.md) · **다음 →** [③ Node.js 설치](nodejs.md)
</div>
