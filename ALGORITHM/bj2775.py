import sys

m = int(sys.stdin.readline())

for i in range(m):
    num_1 = int(sys.stdin.readline())

    # 숫자가 중복되어도 1개만 카운팅되므로 set으로 중복제거해서 시간초과 면하기
    lst_num = set(map(int, sys.stdin.readline().split()))

    num_2 = int(sys.stdin.readline())
    lst_num2 = list(map(int, sys.stdin.readline().split()))
    lst = []
    for i in lst_num2:
        if i in lst_num:
            lst.append(1)
        else:
            lst.append(0)
    print(*lst, sep='\n')
