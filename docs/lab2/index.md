# 실습 2 · 계약서에서 계약종합 만들기

> **한 줄 목표**: 양식이 제각각인 계약서 PDF 8건에서 같은 항목을 뽑아 계약종합 엑셀 한 장으로 만들되, 문서에 없는 값은 지어내지 않는다.

## 오늘 받은 일

> 입사 3주차. 총무팀 사수가 말합니다.
>
> "계약서가 폴더에 PDF로 쌓여 있어요. 계약서마다 형식과 내용이 제각각인데, 하나의 엑셀 파일로 정리해줘요. 계약번호, 계약명, 계약기간, 금액, 자동 갱신 여부, 그리고 계약 상대에 대한 정보는 반드시 포함되어야 해요. 단, 없는 항목을 그럴듯하게 채우면 절대 안 됩니다."

계약서에서 뽑아내야 할 내용을 정리해 AI에게 작업을 맡기고, 그 결과물이 믿을만 한지 **검증**까지 진행해 봅시다.

## 폴더에 있는 것

| 파일 | 무엇 |
|---|---|
| `CT-2026-001.pdf` ~ `CT-2026-008.pdf` | 계약서 8건 |

<div style="display:flex;gap:12px;flex-wrap:wrap">
  <figure style="flex:1 1 0;min-width:200px;margin:0">
    <img src="../images/lab2/contract_example_1.png" alt="contract_example_1.png" style="width:100%;height:auto;display:block">
    <figcaption style="text-align:center;font-size:0.85em;color:#888;margin-top:6px">계약서 예시 1</figcaption>
  </figure>
  <figure style="flex:1 1 0;min-width:200px;margin:0">
    <img src="../images/lab2/contract_example_2.png" alt="contract_example_2.png" style="width:100%;height:auto;display:block">
    <figcaption style="text-align:center;font-size:0.85em;color:#888;margin-top:6px">계약서 예시 2</figcaption>
  </figure>
</div>

## 실습에서 할 일

| 단계 | 할 일 |
|---|---|
| [1단계](step1.md) | 계약서 8건에서 6개 항목을 뽑아 **하나의 파일**로 정리한다 |
| [2단계](step2.md) | 계약종합을 원본과 대조하며 **검산**한다 |
