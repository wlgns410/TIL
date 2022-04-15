# 멀티 프로세싱

멀티 스레드는 여러 worker(스레드)를 만들어 동작하지만, 메모리를 공유해서 1개가 에러나면 다른 것까지 문제가 생긴다.  
이를 해결하기 위해 한 번에 1개의 스레드만 유지하는 락의 개념인 `GIL`이 탄생했다.  
한 스레드가 다른 스레드를 차단해서 제어를 얻는 것을 막아준다.  
멀티 스레드의 위험으로부터 보호를 하는 것이다.  

<br>

파이썬 멀티 스레딩은 동시성을 사용하여 I/O bound에서 유용하게 사용할 수 있다.  
하지만 cpu bound에서는 동시성에서 이점이 없기 때문에 DIL에 의해 동시성밖에 지원을 하지 않는다.  
때문에 cpu bound에서는 멀티 스레딩이 원하는 결과를 얻을 수 없게 된다.

<br>

그래서 사용하는 것이 멀티 프로세싱이다.  
대신에 프로세스를 복제하고 프로세스끼리 메모리 공유를 하지않아서 직렬화, 역직렬화를 해야해서 비용이 크다.  

<br>

```
import time
import os
import threading


nums = nums = [50, 63, 32]

def cpu_bound(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    for num in nums:
        cpu_bound(num)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
```

```
57682 process | 4458520064 thread
57682 process | 4458520064 thread
57682 process | 4458520064 thread

45.376620054244995
```

<br>

일반 코드로 했을 때 45초가 걸렸다.

<br>


```
import time
import os
import threading
import requests
from concurrent.futures import ThreadPoolExecutor




nums = [50, 63, 32]

def cpu_bound(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    excutor = ThreadPoolExecutor(max_workers=10)
    results = list(excutor.map(cpu_bound, nums))
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
```

```
55568 process | 123145455411200 thread
55568 process | 123145460666368 thread
55568 process | 123145465921536 thread
43.706687927246094
```

<br>

멀티 스레드로 했을 때는 43초가 걸렸다. -> 스위칭(병렬성 x)

<br>

시간 차이가 별로 안난다는 것을 알 수 있다.  

<br>

멀티 프로세싱

```
import time
import os
import threading
from concurrent.futures import ProcessPoolExecutor


nums = [50, 63, 32]


def cpu_bound(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total


def main():
    excutor = ProcessPoolExecutor(max_workers=10)
    results = list(excutor.map(cpu_bound, nums))
    print(results)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
```


```
60142 process | 4624350720 thread
60143 process | 4624350720 thread
60144 process | 4624350720 thread

40.26188898086548
```

<br>

`ThreadPoolExecutor` -> `ProcessPoolExecutor`만 고치면 된다.

cpu bound 코드(일반 코드)와 비교하면 5초가 줄었다. 많이 줄었는지는 모르겠지만, cpu bound에서는 동시성에서 이점이 없다는 것 치고는 많이 줄은것이라고 한다.  

cpu bound에서는 멀티 스레드보다는 멀티 프로세싱을 권장한다고 한다.  

<br>
