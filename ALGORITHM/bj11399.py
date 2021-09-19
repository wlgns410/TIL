import sys

num = int(sys.stdin.readline())
k = list(map(int, sys.stdin.readline().split()))
k.sort()

for i in range(num):
    cnt = 0
    lst = []
    for j in k:
        cnt += j
        lst.append(cnt)

print(sum(lst))

    