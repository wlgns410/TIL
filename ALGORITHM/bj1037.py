import sys

num = int(sys.stdin.readline())

k = list(map(int, sys.stdin.readline().split()))

k.sort(reverse=True)
# 최솟값 * 최댓값 = N이 된다.
print(k[0]*k[-1])

    