import sys

q,w,e = map(int, sys.stdin.readline().rstrip().split())

lst = []
lst.append(q)
lst.append(w)
lst.append(e)

lst.sort()
print(*lst, sep=' ')