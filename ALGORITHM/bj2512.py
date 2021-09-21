import sys

n = int(sys.stdin.readline())

num = list(map(int, sys.stdin.readline().rstrip().split()))
k = int(sys.stdin.readline())

start, end = 1, max(num)

while start <= end:
    mid = (start + end) // 2
    money = 0

    # 작은 값을 계속 더해줌
    for i in num:
        money += min(mid, i)
    
    # 목표 이하면 계속 돌림
    if money <= k:
        start = mid + 1
    # 초과하면 돌림
    else:
        end = mid - 1

print(end)