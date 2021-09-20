import sys

N, C = map(int, sys.stdin.readline().rstrip().split())

lst = []
for i in range(N):
    num = int(sys.stdin.readline())
    lst.append(num)
lst = sorted(lst)

# 거리당 공유기 설치
def counter(dis):
    cnt = 1
    home = lst[0]
    for i in range(1, N): # home을 index[0]으로 지정해서 1부터 조회
        if home + dis <= lst[i]:
            cnt += 1
            home = lst[i] # 집 갱신해서 [i]번째부터 다시 조회
    return cnt

# 첫 집과 끝 집
start, end = 1, lst[-1] - lst[0]

# 이진 탐색
while start <= end:
    mid = (start+end)//2
    
    if counter(mid) >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1
print(ans)
