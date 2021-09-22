import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

lst = []
for i in range(n):
    money = int(sys.stdin.readline())
    lst.append(money)

start, end = max(lst), sum(lst)

# end = sum(lst)로 하면 end = mid-1 때문에 499가 출력됨
# 따라서 새롭게 변수를 지정해줘야 함
ans = sum(lst)

while start <= end:
    mid = (start + end) // 2

    # mid는 1, -1 씩 이동해야하는데, mid에서 리스트의 값을 빼줄 변수가 필요함
    charge = mid
    
    num = 1

    for i in range(n):
        if charge < lst[i]:
            num += 1
            charge = mid
            charge -= lst[i]
            
        else:
            charge -= lst[i]



    if num > m:
        start = mid + 1

    else:
        end = mid -1
        # 결과값은 mid보다 큰 총 합을 구하는 것
        if ans > mid:
            ans = end
            
print(ans)
