# 3. Node.js 설치하기

!!! abstract "이 페이지에서 하는 일"
    - 실습 도구를 실행해 주는 프로그램 **Node.js**를 설치합니다
    - 터미널에서 `node --version` · `npm --version`이 숫자를 답하면 통과입니다

- **Node.js**는 자바스크립트로 만든 도구를 여러분 컴퓨터에서 직접 실행할 수 있게 해주는 프로그램입니다.
- 실습에서는 AI 도구 설치 명령(심화 실습의 스킬 설치 등)이 이걸 사용합니다. 직접 다룰 일은 없습니다.


## 다운로드와 설치

Node.js 공식 사이트에 접속합니다.

```
https://nodejs.org
```

**1단계.** 운영체제에 맞는 설치 프로그램을 받아 안내 순서대로 설치합니다.

- **Windows** → `Windows Installer (.msi)`
- **macOS** → `macOS Installer (.pkg)`

설치가 끝나면 아래 [설치 확인](#설치-확인)으로 넘어가세요.

!!! tip "설치 프로그램이 실행되지 않는다면 (Windows)"
    회사 보안 정책 등으로 `.msi` 설치가 막히는 경우가 있습니다. 이때는 아래 **압축 파일로 설치하기**를 따라 하세요.


## 압축 파일로 설치하기 (Windows, 선택)

설치 프로그램이 동작하지 않을 때만 진행하면 됩니다.

**1단계.** 공식 사이트에서 **Standalone Binary (.zip / .gz)**를 받아 압축을 풉니다. 압축이 풀린 **폴더 경로를 복사**해 둡니다.

**2단계.** 윈도우 검색창에 `시스템 환경 변수 편집`을 입력해 실행합니다.

![윈도우 검색창에서 '시스템 환경 변수 편집'을 검색한 화면](../../images/setup/node_1.png)

**3단계.** `고급` 탭에서 **환경 변수** 버튼을 누릅니다.

![시스템 속성 창의 고급 탭 — 아래쪽 환경 변수 버튼](../../images/setup/node_2.png)

**4단계.** 목록에서 `Path`를 선택하고 **편집**을 누릅니다.

![환경 변수 창에서 Path 항목을 선택하고 편집을 누르는 화면](../../images/setup/node_3.png)

**5단계.** **새로 만들기**를 눌러 1단계에서 복사한 폴더 경로를 붙여넣고 **확인**으로 저장합니다.

![환경 변수 편집 창에서 새로 만들기로 폴더 경로를 추가한 화면](../../images/setup/node_4.png)


## 설치 확인

설치가 끝나면 **새 명령 프롬프트(또는 터미널) 창**을 엽니다. 기존에 열려 있던 창은 PATH가 업데이트되지 않았을 수 있습니다.

```bash
node --version
```

!!! success "이렇게 나오면 정상입니다"
    `v20.x.x` 형태의 버전이 출력됩니다.

npm도 함께 설치됐는지 확인합니다.

```bash
npm --version
```

버전 번호가 출력되면 npm도 정상 설치된 것입니다.

!!! warning "`Installation complete!`가 떴는데 버전이 안 나온다면"
    창을 완전히 닫았다가 **새 창**을 열어 같은 명령을 다시 입력하세요. PATH는 새 창부터 반영됩니다.

!!! warning "`npm` 실행 시 보안 오류가 뜬다면 (Windows)"
    명령 프롬프트 창에서 아래와 같은 오류가 뜰 수 있습니다.

    ![PowerShell에서 npm 실행 시 뜨는 PSSecurityException 오류](../../images/setup/pssecurity_exception.png)

    검색 창에 `PowerShell`을 입력해 **관리자 권한으로 실행**한 뒤, 아래 명령을 입력하고 확인 창이 뜨면 `Y`를 누르세요.

    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```

    이후 **새 터미널 창**을 열어 `npm --version`을 다시 실행해보세요.

<div class="stage-nav" markdown>
**← 이전** [② Python 설치](python.md) · **다음 →** [④ AI 에이전트 설치](agent.md)
</div>
