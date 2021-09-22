import sys

n, m = map(int, sys.stdin.readline().split())

lst = []
for i in range(m):
    k = int(sys.stdin.readline())
    lst.append(k)

start, end = 1, sum(lst)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in lst:
        if i % mid == 0:
            cnt += i//mid
        else:
            # 나머지에서 인원수 나누는데, 그 값이 애매해서 1을 더해줬음
            cnt += (i//mid) + 1

    # n명보다 더 많은 보석을 가져갔기 때문에, 적게 가져가기 위해 start 값을 이동시킴
    if cnt > n:
        start = mid + 1
    else:
        end = mid - 1

print(start)
    