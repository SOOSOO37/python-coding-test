def solution(s):
    
    arr = []
    for i in s:
        if len(arr) == 0:
            arr.append(i)  
        else:
            if arr[-1] + i == '()':
                arr.pop()
            else:
                arr.append(i)
    return len(arr)==0
    
