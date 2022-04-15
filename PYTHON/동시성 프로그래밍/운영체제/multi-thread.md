# 멀티 스레딩

`os.getpid()` : 현재 프로세스의 Id를 말한다. 프로세스는 각각의 id가 존재한다.  

```
import requests
import time
import os
import threading


def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://google.com"] * 10

    # with 명령어로 자동 닫기 시킴
    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
```

```
29498 process | 4410998272 url : https://google.com
29498 process | 4410998272 url : https://google.com
29498 process | 4410998272 url : https://google.com
29498 process | 4410998272 url : https://google.com
29498 process | 4410998272 url : https://google.com
29498 process | 4410998272 url : https://google.com
29498 process | 4410998272 url : https://google.com
29498 process | 4410998272 url : https://google.com
29498 process | 4410998272 url : https://google.com
29498 process | 4410998272 url : https://google.com
```

<br>

id : 29498로 프로세스가 10번 호출되었다.  
단일 스레드로 코드가 동작되었다.

<br>

`max_workers` 는 실행할 스레드의 수를 말한다. 1이면 싱글스레드이다.  

<br>

```
import time
import os
import threading
import requests
from concurrent.futures import ThreadPoolExecutor




def fetcher(params):
    session = params[0]
    url = params[1]
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com"] * 100

    executor = ThreadPoolExecutor(max_workers=10)

    with requests.Session() as session:
        params = [(session, url) for url in urls]
        result = list(executor.map(fetcher, params))
        print(result)


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
```

<br>

```
7.128742933273315

```

<br>

스레드를 10개로 늘리고, 호출을 해봤다. -> 멀티 스레딩  
`def fetcher(params):` 처럼 받은 이유는 `session`도 받아야하는데, `urls`를 튜플 형태로 받기 때문에 데이터를 빼내기 위해서 이다.  

<br>