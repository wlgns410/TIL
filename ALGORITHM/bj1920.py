import sys

num_1 = int(sys.stdin.readline())

k_1 = list(map(int, sys.stdin.readline().split()))

num_2 = int(sys.stdin.readline())

k_2 = list(map(int, sys.stdin.readline().split()))

lst = []

for j in k_2:
    if j in k_1:
        lst.append(1)
    else:
        lst.append(0)
print(*lst, sep='\n')


    
