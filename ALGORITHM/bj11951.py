import sys

num = int(sys.stdin.readline())

lst = []
for i in range(num):
    [x,y] = map(int, sys.stdin.readline().split())
    # sorting은 첫 인덱스 좌표순으로 된다. 따라서 위치만 바꿔주면 된다.
    lst.append([y,x])

k = sorted(lst)

for i in range(num):
    print('%d %d' %(k[i][1], k[i][0]))