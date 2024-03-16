def solution(numbers):
    answer = 0
    sum_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(len(sum_list)):
        for j in range(len(numbers)):
            if sum_list[i] == numbers[j]:
                sum_list[i] -= numbers[j]
        
        answer += sum_list[i]

    return answer
