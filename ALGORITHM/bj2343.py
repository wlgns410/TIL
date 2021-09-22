import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

num = list(map(int, sys.stdin.readline().rstrip().split()))

# 최소 레슨들 중 가장 큰값이 되어야 블루레이에 모든 레슨을 담을 수 있다.
# 처음 값은 max(num) = 9이지만, start 값이 바뀌므로 max(num)으로 해야 반복문이 됨
start, end = max(num), sum(num)

# sys.maxsize는 임의의 큰 값을 서서 최소, 최대 범위를 정함
# 10000을 넘지않는다고 했으니 10001로 초기화를 한다.
ans = sum(num)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    sum = 0

    for i in range(len(num)):
        if sum + num[i] > mid:
            cnt += 1
            sum = 0
        sum += num[i]
    if sum:
        cnt += 1


    if cnt > m:
        start = mid + 1
    else:
        ans = min(ans, mid)
        end = mid - 1
        
print(ans)