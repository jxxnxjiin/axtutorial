# 실습 3 · 쿠폰 성과 집계하고 인사이트 뽑기

> **한 줄 목표**: 다섯 개 채널의 서로 다른 주문 기록을 한 파일로 모은 뒤, 쿠폰 성과표로 정리하고 "그래서 뭘 해야 하는지" 인사이트를 도출한다.

## 오늘 받은 일

> 입사 3주차. 마케팅팀 사수가 말합니다.
>
> "지난 반년 동안 쿠폰 44종을 뿌렸는데, 어떤 게 남고 어떤 게 밑지는지 아무도 몰라요. 주문 기록이 **채널 다섯 곳에서  따로** 집계돼요. 이걸 한 파일로 모아 쿠폰별 성과표를 채우고, **그래서 어떤 쿠폰을 접고 어떤 쿠폰을 더 발행할지** 인사이트까지 정리해줘요. 우리 마진은 매출의 30%로, **취소된 주문은 빼고** 계산해요."

먼저 다섯 파일을 **하나로 모으고** 쿠폰별로 **줄인**(집계) 뒤, 표에서 **인사이트**를 뽑아봅시다.

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
| [1단계](step1.md) | 채널 5곳 원본을 **한 파일로 모은다** |
| [2단계](step2.md) | **쿠폰별 성과표**를 채운다 |
| [3단계](step3.md) | 원본과 대조하며 **집계를 검산**한다 |
| [4단계](step4.md) | 표에서 **인사이트를 뽑고**, 지어낸 해석이 없는지 검증한다 |
