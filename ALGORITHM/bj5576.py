import sys

lst = []
for i in range(20):
    num = int(sys.stdin.readline())
    lst.append(num)

lst1 = lst[0:10]
lst2 = lst[10:]

lst1.sort()
lst2.sort()

ans1 = sum(lst1[-3:])
ans2 = sum(lst2[-3:])

print(ans1, ans2)
