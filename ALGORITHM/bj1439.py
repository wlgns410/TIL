import sys

k = sys.stdin.readline().rstrip()
cnt = 1
start = k[0]
# len(k)-1을 하면 k의 인덱스를 i와 i+1을 비교할 수 있음
for i in range(1, len(k)):
    if k[i] != start:
        cnt += 1
        start = k[i]

# 길이에 상관없이 몇번 바뀌는지만 봄
# 길이의 절반을 나눠서 몫을 구하면 자동적으로 짝수 or 홀수 중 작은 값을 선택함
print((cnt)//2)