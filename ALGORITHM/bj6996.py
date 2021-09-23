import sys

num = int(sys.stdin.readline())

for i in range(num):
    a, b = map(str, sys.stdin.readline().split())
    
    a1 = sorted(list(a))
    b1 = sorted(list(b))

    if a1 == b1:
        print("%s & %s are anagrams." %(a, b))
    else:
        print("%s & %s are NOT anagrams." %(a, b))