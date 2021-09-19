import sys

num = int(sys.stdin.readline())

lst = []
for i in range(num):
    k = int(sys.stdin.readline())
    lst.append(k)

# 큰 값부터 순서대로 나오게 내림차순 정렬
lst.sort(reverse=True)

# 가장 작은 무게를 들 수 있는 로프가 들 수 있는 질량 * 병렬 연결 로프 갯수 = 최종 무게
# ex) 15 10 일 경우 15 x 1, 10 x 2 -> 10 x 2가 가장 큰 값
for i in range(num):
    lst[i] = lst[i] * (i+1)

print(max(lst))