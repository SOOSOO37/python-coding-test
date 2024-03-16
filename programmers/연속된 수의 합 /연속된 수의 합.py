def solution(num, total):
    answer = []
    mid = total // num
    m = (num - 1) // 2
    for i in range(num):
        answer.append(mid + i - m)
    return answer
