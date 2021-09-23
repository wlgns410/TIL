import sys

n, m = map(int, sys.stdin.readline().split())

lst1 = []
for i in range(n):
    word1 = sys.stdin.readline()
    lst1.append(word1)

lst2 = []
for i in range(m):
    word2 = sys.stdin.readline()
    lst2.append(word2)

# 교집합 합집합은 튜플형태만 가능
result = sorted(list(set(lst1).intersection(lst1, lst2)))
print(len(result))
for i in result:
    print(i, end='')
