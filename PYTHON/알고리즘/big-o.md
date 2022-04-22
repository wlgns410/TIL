# big-o
쉽게 말하면 알고리즘 성능 측정기

<br>

```
def big_o(arr):

    print(arr)

big_o([1,2,3])
```
문제를 해결하는데 오직 한 단계만 처리한다. 입력받고 출력한다.  
이는 O(1)이라고 한다. 즉 연산횟수 고정이다.  

입력에 관계없이 복잡도는 동일하다고 한다.  

<br>

위키피디아를 참조했다.  

```
def binarySearch(array, value, low, high):
	if low > high:
		return False
	mid = (low+high) / 2
	if array[mid] > value:
		return binarySearch(array, value, low, mid-1)
	elif array[mid] < value:
		return binarySearch(array, value, mid+1, high)
	else:
		return mid
```

입력의 절반을 찾지않고 지나가는 알고리즘  
알고리즘의 실행 시간이 입력 크기의 로그에 비례한다.  

주로 이진탐색이라고 한다.  



<br>

```
def big_o(arr):
    for item in arr:
        print(item * item)

big_o([1,2,3])
```

리스트의 크기가 n개면 n 번 만큼 실행되므로 O(n)이라고한다.  
O(2n) O(3n)... 이든 상관없이 O(n)만 표기한다.

<br>

```
def big_o(arr):
    for item1 in arr:
        for item2 in arr:
            print(item1 * item2)

big_o([1,2,3])
```

위와 같은 구조는 리스트 크기가 n개면 n * n번 만큼 실행된다.  
그래서 O(n^2)라고 한다.

<br>



```
성능
[Excellent] O(1) < O(logn) < O(n) < O(n log n) < O(n2) < O(2n) [Horrible]
```