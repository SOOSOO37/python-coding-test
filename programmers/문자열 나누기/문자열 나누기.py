def solution(s):
    answer = 0
    init = s[0]
    count = 0
    for c in s:
        if count == 0:
            init = c
        if init == c:
            count += 1
        else:
            count -= 1
        if count == 0:
            answer += 1
    
    if count > 0:
        answer += 1
    
    return answer
