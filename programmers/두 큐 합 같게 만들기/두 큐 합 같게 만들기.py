from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)
    total = sum1+sum2

    if total % 2 == 1:
        return -1

    move =0

    for i in range(4 * len(queue1) + 1):
        if sum1 < sum2:
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
            move +=1
        elif sum1 > sum2:
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
            move +=1
        else:
            return move

    return -1
