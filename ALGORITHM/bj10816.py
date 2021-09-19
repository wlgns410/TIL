import sys

# 상근이가 가지고 있는 카드
num_1 = int(sys.stdin.readline())
card_1 = list(map(int, sys.stdin.readline().rstrip().split()))

# dict에 가지고 있는 카드의 개수와 숫자를 담는다.
dict_1 = dict()

for i in card_1:
    if i in dict_1:
        dict_1[i] += 1
    else:
        dict_1[i] = 1

# dict에 담은 카드와 입력받은 카드를 비교
num_1 = int(sys.stdin.readline())
card_2 = list(map(int, sys.stdin.readline().rstrip().split()))

for i in card_2:
    # 주어진 dict에서 key값을 찾아 value를 출력하고 없으면 0을 출력
    if i in dict_1:
        print(dict_1[i], end=' ')
    else:
        print(0, end=' ')