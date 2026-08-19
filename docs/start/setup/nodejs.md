# 3. Node.js 설치하기

!!! abstract "이 페이지에서 하는 일"
    - 실습 도구를 실행해 주는 프로그램 **Node.js**를 설치합니다
    - 터미널에서 `node --version` · `npm --version`이 숫자를 답하면 통과입니다

- **Node.js**는 자바스크립트로 만든 도구를 여러분 컴퓨터에서 직접 실행할 수 있게 해주는 프로그램입니다.
- 실습에서는 AI 도구 설치 명령(심화 실습의 스킬 설치 등)이 이걸 사용합니다. 직접 다룰 일은 없습니다.


## Windows에서 설치하기

Windows에서 가장 간단한 방법은 공식 설치 프로그램을 쓰는 것입니다.

### 방법 1: 설치 프로그램 다운받기

Node.js 공식 사이트에 접속합니다.

```
https://nodejs.org
```
**Windows 설치 프로그램(.msi)**을 받고, 안내 순서에 따라 프로그램을 설치합니다. 만약 설치가 되지 않는다면 아래 방법에 따라 설치를 진행할 수 있습니다. 

### 방법 2: binary 파일 다운받기

**Standalone Binary(.gz)**를 받고, 압축 파일을 해제합니다. 압축 해제된 폴더의 경로를 복사해둡니다. 

1. 윈도우 검색창에서 "시스템 환경 변수 편집"을 선택합니다. 
![node1](../../images/setup/node_1.png)

2. 고급 > 환경변수
![node2](../../images/setup/node_2.png)

3. Path 부분을 누르고 편집을 누릅니다. 
![node3](../../images/setup/node_3.png)

4. 환경변수 편집 부분에서 새로 만들기를 누르고, 아까 복사했던 폴더의 경로를 입력 후 저장합니다.
![node4](../../images/setup/node_4.png)


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
