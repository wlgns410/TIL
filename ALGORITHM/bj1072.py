import sys

k,m = map(int, sys.stdin.readline().rstrip().split())

vic = (m*100)//k
# 포인터 사이즈를 리턴(구조의 길이 제한 지정)
ans = sys.maxsize
# 최대값은 K 입력값
start, end = 1, k

while start <= end:
    mid = (start+end)//2
    win = (m + mid) * 100 // (k + mid)

    if win <= vic:
        start = mid +1
    else:
        # 작은 값을 반환해서 계속 돌림
        ans = min(mid, ans)
        end = mid - 1

# 길이 제한을 넘겨버리면
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)