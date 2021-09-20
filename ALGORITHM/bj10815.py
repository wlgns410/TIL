import sys

num_1 = int(sys.stdin.readline())
card_1 = list(map(int, sys.stdin.readline().rstrip().split()))

dt = dict()

for i in card_1:
    if i in dt:
        dt[i] += 1
    else:
        dt[i] = 1

num_2 = int(sys.stdin.readline())
card_2 = list(map(int, sys.stdin.readline().rstrip().split()))

for i in card_2:
    if i in dt:
        print(dt[i], end=' ')
    else:
        print(0, end=' ')