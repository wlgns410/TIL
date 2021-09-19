import sys

num, all = map(int, sys.stdin.readline().rstrip().split())
tree = list(map(int, sys.stdin.readline().split()))

start , end = 0, max(tree)

while start <= end:
    mid = (start + end) // 2
    cut = 0
    for i in tree:
        if i >= mid:
            cut += i - mid

    if cut >= all:
        start = mid + 1
    else:
        end = mid - 1
print(end)
