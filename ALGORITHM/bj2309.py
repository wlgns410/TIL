import sys

lst = []
for i in range(9):
    k = int(sys.stdin.readline())
    lst.append(k)
all = sum(lst)

num = []
for i in range(9):
    for j in range(i+1, 9):
        if 100 == all - (lst[i]+lst[j]):
            num1, num2 = lst[i], lst[j]

            # del은 번호를 알 때 사용하고, remove는 번호를 모를 때 사용
            lst.remove(num1)
            lst.remove(num2)
            lst.sort()

            for i in range(len(lst)):
                print(lst[i])
            # 범위를 넘지않게 len의 개수를 다 세고나서 break 걸어줘야함         
            break

    # 여기도 7일 때 break를 걸어줘야함. 이미 7개가 됐는데 range는 9 까지니까 범위 초과
    if len(lst) ==7:
        break


