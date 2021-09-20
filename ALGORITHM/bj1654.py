import sys

K, N = map(int, sys.stdin.readline().rstrip().split())

lst = []
for i in range(K):
    num = int(sys.stdin.readline())
    lst.append(num)

# start=0으로 지정하면 ZeroDivisionError 발생
start, end = 1, max(lst)

while start <= end:
    mid = (start + end) // 2
    lan = 0

    for i in lst:
        lan += i // mid

    if lan >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)


