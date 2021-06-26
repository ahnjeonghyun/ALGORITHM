# prices는 배열이며, 각 요소는 매일의 주식 가격입니다. 만약 한 번만 거래할 수 있다면 = 사고 팔 수 있다면, 제일 큰 이익은 얼마일까요?
def maxProfit(prices):
  min_value = min(prices)
  a=[]
  for i in prices:

    if prices.index(min_value) < prices.index(i):
      a.append(i - min_value)

  if len(a) <= 0:
    return 0

  return 0 if max(a) <= 0 else max(a) 