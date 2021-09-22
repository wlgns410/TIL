import sys
from bisect import bisect_right 

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    num_1, num_2 = map(int, sys.stdin.readline().rstrip().split())
    input_1 = list(map(int, sys.stdin.readline().rstrip().split()))
    input_2 = list(map(int, sys.stdin.readline().rstrip().split()))
    # 오름차순으로 나열 -> 이진탐색 사용하기 위함
    input_1.sort()
    input_2.sort()
    
    cnt = 0
    # 오름차순으로 정렬된 리스트에서 데이터를 삽입할 가장 오른쪽 인덱스를 찾음
    # input_1 원소가 input_2의 i 원소보다 크다면, input_2[i]번째 이후에 있는 모든 원소를 빼주면 input_1이 input_2보다 큰 쌍을 구할 수 있다.
    for i in input_2:
        cnt += len(input_1) - bisect_right(input_1, i)

    print(cnt)



