import sys

n = int(sys.stdin.readline())

# 매트릭스 구조 만들기
graph = [[] * (n+1) for _ in range(n+1)]
# 미방문을 0으로 두고 visit했으면 1이 되는 것을 count하기 위함
visit = [0] * (n+1)

m = int(sys.stdin.readline())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # graph[a][b], graph[b][a] 를 만드는 과정 -> 좌표를 생성한다.
    graph[a].append(b)
    graph[b].append(a)

cnt = 0

# start라는 매개변수를 넣을 것 start = 1(첫줄)이 될 예정
def dfs(start):
    # for문 안에서 cnt를 쓰기 위해 global 선언
    global cnt
    # 방문시 visit = 1
    visit[start] = 1
    for i in graph[start]:
        # visit = 0일때 미방문이라 dfs(i)순번대로 방문하여 count를 1씩 증가시킴
        if visit[i] == 0:
            dfs(i)
            cnt += 1
# 인수는 1
dfs(1)
print(cnt)