def solution(phone_number):
    rear_num  = phone_number[-4:]
    front_num = phone_number[:-4]
    answer = len(front_num) * '*' + rear_num
    
    return answer

solution("01030908382")