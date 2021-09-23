import sys

num = int(sys.stdin.readline())

lst = []
for i in range(num):
    [x ,y] = map(str, sys.stdin.readline().split())
    lst.append([int(x), y])

# sorted를 쓰면 나이, 이름 모두 정렬됨
# 따라서 key를 지정해 리스트의 첫번째 인자인 나이로만 정렬
k = sorted(lst, key=lambda x: x[0])

for i in range(num):
    print('%d %s' %(k[i][0], k[i][1]))