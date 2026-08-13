# 4. AI 코딩 에이전트(Claude Code) 설치하기

!!! abstract "이 페이지에서 하는 일"
    - VS Code에 **Claude Code**를 설치하고 로그인합니다
    - 파일을 고칠 때마다 뜨는 확인 창을 미리 꺼둡니다 **(자동 승인)**

오늘 말을 걸 상대인 **AI 코딩 에이전트**를 설치합니다. VS Code 확장 프로그램으로 설치하면 친숙한 채팅 UI로 바로 시작할 수 있습니다.

## 1. Claude Code 확장 설치

1. 아래 링크에서 Claude Code 확장 페이지를 엽니다.

   ```
   https://marketplace.visualstudio.com/items?itemName=Anthropic.claude-code
   ```
2. 열린 페이지에서 **`VS Code용 설치`** 버튼을 누릅니다.

   ![마켓플레이스에서 VS Code용 설치 버튼 클릭](../../images/setup/claude_install_vscode.png)
3. VS Code가 열리며 확장 페이지가 뜹니다. **`Install`** 버튼을 눌러 설치합니다.

   ![VS Code 확장 페이지에서 Install 버튼 클릭](../../images/setup/claude_install_button.png)

## 2. 로그인

설치가 끝나면 <kbd>Ctrl</kbd>+<kbd>L</kbd> (맥은 <kbd>Cmd</kbd>+<kbd>L</kbd>)을 누릅니다. 오른쪽 패널에 Claude Code 화면이 뜹니다. 여기서 **`Claude.ai Subscription`**(구독 계정 로그인)을 눌러 로그인합니다. 안내대로 브라우저에서 로그인하면 됩니다.

![오른쪽 Claude Code 패널에서 Claude.ai Subscription 로그인](../../images/setup/claude_login_panel.png)

!!! success "이렇게 나오면 정상입니다"
    로그인 후 패널에 입력줄이 뜨고, 말을 걸 수 있는 상태가 됩니다.

!!! warning "이렇게 나왔다면"
    - 로그인이 더 진행되지 않는다 → 계정 문제일 수 있습니다. 운영진에게 연락하세요. 당일 예비 계정을 받을 수 있습니다.

!!! tip "실습 폴더 여는 법"
    실습을 시작할 때는 VS Code 왼쪽 상단 **`Open Folder`**로 실습 자료가 있는 폴더를 열고, 그 상태에서 Claude Code에 질문하면 됩니다.

??? note "CLI 모드로도 쓰고 싶다면 (선택 — 추가 설치 필요)"
    VS Code 확장으로 설치한 Claude Code는 **VS Code 안에서만** 쓸 수 있습니다. 터미널에서 좀 더 자유롭게 쓰고 싶다면 CLI 모드를 추가로 설치합니다.

    **1단계.** 검색 창에 `명령 프롬프트`를 입력해 실행합니다.

    **2단계.** 아래 명령을 입력하고 <kbd>Enter</kbd> (Windows 기준).

    ``bash     curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd     ``

    **3단계.** 아래 명령으로 버전이 출력되면 설치 완료입니다.

    ``bash     claude --version     ``

    `Installation complete!` 가 떴는데도 버전이 안 나오면, 명령 프롬프트를 닫았다가 다시 열어 `claude --version` 을 입력해보세요.

## 3. 확인 창 미리 꺼두기 (자동 승인)

AI가 파일을 고칠 때마다 *"이 파일을 수정해도 될까요?"* 하고 물어봅니다. 오늘 하루는 파일을 수백 번 고치므로, 미리 꺼두면 실습 흐름이 끊기지 않습니다.

!!! tip "설정 방법은 부록에서"
    Claude Code 모드 드롭다운에서 `Edit automatically`를 고르면 됩니다. 명령 실행까지 자동으로 넘기는 방법과 되돌리는 법은 [**부록 · 자동 허가 모드 설정**](autoapprove.md)에 정리해뒀습니다.

## 다 됐는지 스스로 확인하기

- [ ] VS Code에서 Claude Code 패널이 뜨고, **로그인 화면 없이** 말을 걸 수 있다
- [ ] 터미널에서 `python --version` · `node --version` 이 숫자를 답한다
- [ ] Claude Code 패널 아래에 `Edit automatically` 라벨이 보인다

여기까지 됐으면 도구 설치는 끝입니다. 이제 실습 데이터를 준비합니다.

<div class="stage-nav" markdown>
**← 이전** [③ Node.js 설치](nodejs.md) · **다음 →** [⑤ 실습 데이터 준비](data.md)
</div>
