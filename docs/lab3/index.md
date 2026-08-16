# 실습 3 · 쿠폰 성과 집계하고 인사이트 뽑기

> **한 줄 목표**: 다섯 개 채널의 서로 다른 주문 기록을 한 파일로 모은 뒤, 쿠폰 성과표로 정리하고 "그래서 뭘 해야 하는지" 근거에 기반한 인사이트를 도출한다.

## 오늘 받은 일

> 입사 3주차. 마케팅팀 사수가 말합니다.
>
> "지난 반년 동안 쿠폰 44종을 뿌렸는데, 어떤 게 남고 어떤 게 밑지는지 아무도 몰라요. 주문 기록이 **채널 다섯 곳에서 따로** 집계돼요. 이걸 한 파일로 모아 쿠폰별 성과표를 채우고, **그래서 어떤 쿠폰을 접고 어떤 쿠폰을 더 발행할지** 인사이트까지 정리해줘요. 우리 마진은 매출의 30%로, **취소된 주문은 빼고** 계산해요."

쿠폰·이벤트를 뿌리기는 쉬워도 어떤 게 남는 장사였는지는 아무도 모르는 상황. 마케팅 부서에서 흔히 생기는 일입니다. [실습 1](../lab1/index.md)·[실습 2](../lab2/index.md)에서 배운 데이터 모으기로 다섯 파일을 하나로 만들고, 이번에 새로 배우는 자료 요약으로 9천여 건의 데이터를 쿠폰 44줄로 줄입니다.

그런데 표를 들고 가면 팀장님은 "그래서 이 쿠폰들, 왜 적자야?"라고 묻습니다. 숫자는 '무엇'만 보여주고 '왜'는 안 알려주니, 마지막에는 표를 해석해 "그래서 뭘 해야 하는지" **인사이트**까지 뽑습니다. 끝나면 검증까지 마친 성과표와 행동 제안이 남습니다.

## 폴더에 있는 것

| 파일 | 무엇 |
|---|---|
| `1~5.주문기록_*.xlsx` | 채널 5곳 주문 기록 |
| `7.쿠폰별성과표.xlsx` | 채워 넣을 집계표 |

<div style="display:flex;gap:12px;flex-wrap:wrap">
  <figure style="flex:1 1 0;min-width:200px;margin:0">
    <img src="../images/lab3/channel_data_example.png" alt="channel_data_example.png" style="width:100%;height:auto;display:block">
    <figcaption style="text-align:center;font-size:0.85em;color:#888;margin-top:6px">채널별 주문 기록</figcaption>
  </figure>
  <figure style="flex:1 1 0;min-width:200px;margin:0">
    <img src="../images/lab3/coupon_table_empty.png" alt="coupon_table_empty.png" style="width:100%;height:auto;display:block">
    <figcaption style="text-align:center;font-size:0.85em;color:#888;margin-top:6px">채워 넣을 성과표</figcaption>
  </figure>
</div>

## 실습에서 할 일

| 단계 | 할 일 |
|---|---|
| [1단계](step1.md) | 채널 5곳 원본을 **하나의 표**로 모은다 |
| [2단계](step2.md) | **쿠폰별 성과표**를 채운다 |
| [3단계](step3.md) | 원본과 대조하며 **집계를 검산**한다 |
| [4단계](step4.md) | 표에서 **인사이트를 뽑고**, 지어낸 해석이 없는지 검증한다 |
