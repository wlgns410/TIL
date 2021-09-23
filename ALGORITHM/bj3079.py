import sys

n, m = map(int, sys.stdin.readline().split())

lst = []
for i in range(n):
    k = int(sys.stdin.readline())
    lst.append(k)

# 시간 합 * 인원수가 최대값
start, end = min(lst), sum(lst) * m
ans = sum(lst) * m
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in range(n):
        cnt += mid // lst[i]

    # m보다 적은 인원을 심사하면 안되므로 범위만 줄임
    if cnt < m :
        start = mid + 1
    else:
        ans = min(ans, mid)
        end = mid - 1

print(ans)