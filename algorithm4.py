# 주어진 숫자 배열에서, 0을 배열의 마지막쪽으로 이동시켜주세요. 원래 있던 숫자의 순서는 바꾸지 말아주세요.

# 새로운 배열을 생성해서는 안 됩니다.

def move_zeroes(nums):
  for i in nums:
    if i == 0:
      nums.remove(i)
      nums.append(i)

  return nums

move_zeroes([0,1,0,3,12])