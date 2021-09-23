import sys

# 문자열로 받으면 나중에 정수로 바꿀 수가 없음
num = int(sys.stdin.readline())

lst = []
# 정수를 문자열로 바꿔야 인덱스를 가질 수 있음
for i in str(num):
    k = int(i)
    lst.append(k)

lst.sort(reverse=True)

for i in lst:
    print(i, end='')