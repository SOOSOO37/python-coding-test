def solution(arr):
    answer = [arr[0]]
    for a in arr:
        if not a == answer[-1]:
            answer.append(a)
    print('Hello Python')
    return answer
