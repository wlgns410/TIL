import sys

num = int(sys.stdin.readline())

lst = []

for i in range(num):
    [k, m] = map(int, sys.stdin.readline().split())
    lst.append([k, m])

# key에 튜플로 여러 인자를 주면 해당 인자의 순서대로 정렬함
# 끝 시간(m)을 오름차순으로 정렬하고 그 안에서 시작 시간(k)을 오름차순 정렬
x = sorted(lst, key=lambda x: (x[1],x[0]))
cnt = 1
end = x[0][1]

# 첫번째 값은 제외하고 시작
for i in range(1, num):
    if x[i][0] >= end:
        cnt += 1
        end = x[i][1]
print(cnt)