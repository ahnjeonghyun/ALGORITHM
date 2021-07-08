# 다음과 같이 input이 주어졌을 때, 같은 알파벳으로 이루어진 단어끼리 묶어주세요.

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

def groupAnagrams(strs):
    # 여기에 코드를 작성해주세요.
  List1 = {}

  for i in strs:
    key = tuple(sorted(i))
    List1[key] = List1.get(key,[]) + [i]
  
  return list(List1.values())

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])