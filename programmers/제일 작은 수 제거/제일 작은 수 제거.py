def solution(arr):
    length = len(arr)
    
    if length == 1:
        return [-1]
    else:
        min_val = arr[0]
        index = 0
        
        for i in range(length):
            if arr[i] < min_val:
                min_val = arr[i]
                index = i
        
        answer = []
        for j in range(length):
            if j != index:
                answer.append(arr[j])
        
        return answer
