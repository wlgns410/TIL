import sys

num = int(sys.stdin.readline().rstrip())

# 이분 탐색
start, end = 0, num

while start <= end:

    # 제곱근일 때 마지막 자리수에서 1이 반올림될 때 적게 나올 수도 있고 크게 나올 수도 있다.
    mid = (start + end) // 2
    
    # 작게 나오면 1을 더해줘야 함
    if mid ** 2 < num:
        start = mid + 1
        
    # 크게 나왔다면 1을 빼줘야 함
    else:
        end = mid - 1

print(start)
