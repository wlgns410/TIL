num = int(input())

start = 0
last = num

while start <= last:
    mid = (start + last) // 2
    if mid ** 2 < num:
        start = mid + 1
    else:
        last = mid - 1
print(start)