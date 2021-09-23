import sys

num = int(sys.stdin.readline())

lst = []
for i in range(num):
    word = sys.stdin.readline()
    lst.append(word)

# 중복 제거 후 다시 리스트화
lst = list(set(lst))

srt = []
for i in lst:
    srt.append((len(i), i))

# len(i)로 길이 순서대로 sort이 되었음
result = sorted(srt)

# len(i)는 필요없고 i만 출력되면 됨
# 키:값 형식으로 출력되므로 length를 없애고 출력하려면 end로 없애주면 됨
for length, i in result:
    print(i, end='')

    

