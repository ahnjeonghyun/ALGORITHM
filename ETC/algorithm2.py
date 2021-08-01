def solution(s):
    if len(s) % 2 == 1:
        center = len(s) // 2
        result = s[center]
        
    else:
        center = len(s) // 2
        result = s[center-1:center+1]
        
    return result
solution("ABCDEFG") 
