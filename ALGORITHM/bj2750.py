import sys

num = int(sys.stdin.readline())

lst = []
for i in range(num):
    k = int(sys.stdin.readline())
    lst.append(k)

lst.sort()
print(*lst, sep='\n')
