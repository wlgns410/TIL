import sys

q,w,e,r = map(int, sys.stdin.readline().split())

lst = []
lst.append(q)
lst.append(w)
lst.append(e)
lst.append(r)
lst.sort()

ans = lst[0] * lst[-2]
print(ans)
