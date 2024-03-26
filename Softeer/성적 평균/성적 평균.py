N, K = map(int, input().split())

score = [-1] + list(map(int, input().split()))

for _ in range(K):
    start, end = map(int, input().split())
    total = sum(score[start:end + 1])
    average = total/ (end - start + 1)
    print(f'{average:.2f}')
