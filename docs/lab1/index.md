# 실습 1 · 흩어진 주문 한 표로 모으기

> **한 줄 목표**: 웹·전화·제휴 세 경로로 따로 들어온 주문 파일을, 양식이 제각각인데도 표준 7칸짜리 엑셀 한 장으로 합치되 한 건도 빠뜨리거나 지어내지 않는다.

## 오늘 받은 일

> 입사 3주차. 영업지원팀 사수가 말합니다.
>
> "주문이 웹·전화·제휴 세 군데로 따로 들어와요. 파일이 세 개인데 양식이 다 달라요 — 어떤 건 제목이 한글, 어떤 건 영어예요. 이걸 하나의 주문종합 표로 합쳐줘요. 한 건도 빠지면 안 되고, 없는 값을 지어내도 안 됩니다."

웹은 '주문번호', 전화는 'order_id', 제휴는 '협력사주문ID' — 같은 뜻인데 이름이 제각각인 파일이 채널마다 쌓이는 건 어느 회사에서나 벌어지는 일입니다. 몇백 건이면 손으로도 되지만 실제 업무에서 수만 건이 되면 몇 시간짜리 일이 됩니다. 이 첫 실습에서는 그 일을 AI에게 통째로 맡기는 법을 배웁니다 — 빠뜨리지 않는다, 맘대로 바꾸지 않는다, 없는 건 지어내지 않는다는 세 원칙을 규칙으로 넘겨서요. 끝나면 표준 7칸짜리 주문종합 한 장이 나오고, 새거나 겹친 건이 없는지 **검산**까지 마칩니다.

## 폴더에 있는 것

| 파일 | 무엇 |
|---|---|
| `웹주문.xlsx` | 웹으로 들어온 주문 150건 |
| `전화주문.xlsx` | 전화로 받은 주문 140건 |
| `제휴주문.xlsx` | 제휴사가 넘긴 주문 120건 |
| `작업방법참고.xlsx` | 작업 방법, 세 파일 열 이름 대조표 |
| `주문종합.xlsx` | 채워 넣을 빈 템플릿 |

<div style="display:flex;gap:12px;flex-wrap:wrap">
  <figure style="flex:1 1 0;min-width:180px;margin:0">
    <img src="../images/lab1/orders_example_1.png" alt="orders_example_1.png" style="width:100%;height:320px;object-fit:cover;object-position:top;display:block">
    <figcaption style="text-align:center;font-size:0.85em;color:#888;margin-top:6px">웹주문</figcaption>
  </figure>
  <figure style="flex:1 1 0;min-width:180px;margin:0">
    <img src="../images/lab1/orders_example_2.png" alt="orders_example_2.png" style="width:100%;height:320px;object-fit:cover;object-position:top;display:block">
    <figcaption style="text-align:center;font-size:0.85em;color:#888;margin-top:6px">전화주문</figcaption>
  </figure>
  <figure style="flex:1 1 0;min-width:180px;margin:0">
    <img src="../images/lab1/orders_example_3.png" alt="orders_example_3.png" style="width:100%;height:320px;object-fit:cover;object-position:top;display:block">
    <figcaption style="text-align:center;font-size:0.85em;color:#888;margin-top:6px">제휴주문</figcaption>
  </figure>
</div>

## 실습에서 할 일

| 단계 | 할 일 |
|---|---|
| [1단계](step1.md) | 세 파일의 내용을 **엑셀 한 장으로 합친다** |
| [2단계](step2.md) | 빠지거나 겹친 건이 없는지 원본과 대조하며 **검산**한다 |
