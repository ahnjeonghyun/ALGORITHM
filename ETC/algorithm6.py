# 양수 N을 이진법으로 바꿨을 때, 연속으로 이어지는 0의 갯수가 가장 큰 값을 return해 주세요.

# 이어지는 0은 1과 1사이에 있는 것을 의미합니다.
# 이런 것을 binary gap 이라고 합니다.

def solution(N):

  N     = format(N, 'b')
  stack = []
  count = []
  if len(N) <= 2:
    return 0

  for i in enumerate(N):
    if stack:
      if i[1] == '0':
        stack.append(i[1])

      if i[1] == '1':
        count.append(stack.count('0'))
        stack.clear()
        stack.append(i[1])

    else:
      stack.append(i[1])
    
  if len(count) == 0:
    return 0

  return max(count)
solution(9)