# 인자인 height는 숫자로 이루어진 배열입니다.그래프로 생각한다면 y축의 값이고, 높이 값을 갖고 있습니다.

# 아래의 그래프라면 height 배열은 [1, 8, 6, 2, 5, 4, 8, 3, 7] 입니다.

# https://storage.googleapis.com/replit/images/1555380144403_97221ca23fbb92beaae5b6c800ceb5c8.pn

# 저 그래프에 물을 담는다고 생각하고, 물을 담을 수 있는 가장 넓은 면적의 값을 반환해주세요.

def get_max_area(height):
  index=[i for i in enumerate(height)]
  
  c = []
  for i in range(len(height)):
    for j in range(i+1, len(height)):
      left   = index[i][1]
      right  = index[j][1]
      h = min(left,right)
      length = index[j][0] - index[i][0]
      c.append(length * h)

  return max(c)


get_max_area([1, 8, 6, 2, 5, 4, 8, 3, 7])