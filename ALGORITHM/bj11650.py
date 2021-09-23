import sys

num = int(sys.stdin.readline())

lst = []
for i in range(num):
    # x,y를 좌표로 입력해서 리스트에 집어넣음
    [x,y] = map(int, sys.stdin.readline().split())
    lst.append([x,y])

x = sorted(lst)

for i in range(num):
    # 0열은 x좌표 1열은 y좌표가 출력됨
    print('%d %d' %(x[i][0],x[i][1]))
