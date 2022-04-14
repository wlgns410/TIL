# 코루틴을 이용해서 웹크롤링을 해보자.

세션을 이용해 서버와 클라이언트 연결을 유지시킬 것이다.  
네이버 접속 후, 세션을 유지시키고  
requests.get 을 통해 데이터를 긁어온다.  

<br>

```
import requests


# text를 모두 긁어옴
def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    url = "https://naver.com"

    """
    # session = requests.Session()
    # 세션을 오픈
    # session.get(url)
    # 세션을 닫아줌
    # session.close(url)
    """

    # with 명령어로 자동 닫기 시킴
    with requests.Session() as session:
        result = fetcher(session, url)
        print(result)


if __name__ == "__main__":
    main()

```

```

...

ttps://recruit.navercorp.com/naver/recruitMain" data-clk="recruit">인재채용</a></li> <li class="corp_item"><a href="https://www.navercorp.com/naver/proposalGuide" data-clk="contact">제휴제안</a></li> <li class="corp_item"><a href="/policy/service.html" data-clk="service">이용약관</a></li> <li class="corp_item"><a href="/policy/privacy.html" data-clk="privacy"><strong>개인정보처리방침</strong></a></li> <li class="corp_item"><a href="/policy/youthpolicy.html" data-clk="youth">청소년보호정책</a></li> <li class="corp_item"><a href="/policy/spamcheck.html" data-clk="policy">네이버 정책</a></li> <li class="corp_item"><a href="https://help.naver.com/" data-clk="helpcenter">고객센터</a></li> </ul> <address class="addr"><a href="https://www.navercorp.com" target="_blank" data-clk="nhn">ⓒ NAVER Corp.</a></address> </div> </div> </div> </div> <div id="adscript" style="display:none"></div> </body> </html>
```

<br>

만약 url이 여러개라면?

```
import requests


def fetcher(session, url):
    with session.get(url) as response:
        return response.text


def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10


    # session = requests.Session()
    # 세션을 오픈
    # session.get(url)
    # 세션을 닫아줌
    # session.close(url)

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
12.276936292648315
```

사이트 3개에서 10번씩 긁어오다보니 블로킹에 걸리고 시간이 좀 걸렸다.  
더 많은 사이트에서 동시에 긁어오면 더 시간이 걸릴 것이다.

<br>

# 비동기 - 코루틴 사용

우선 `requests` 모듈은 동기적으로 작동하는 모듈이므로 사용하지 않는다.  
대신 코루틴을 사용한 `AIOHTTP` 모듈을 사용한다.  

<br>

> pip install aiohttp

설치하고  

<br>

공식문서에 나와있는 예시이다.  
이 코드를 따라서 기존 코드를 수정해보자.  

```
import aiohttp
import asyncio

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

<br>

`aiohttp`로 클라이언트 세션을 열어준다  
`async with session.get('http://python.org') as response:`로 세션을 받는다.  
나는 이게 fetcher 함수에 작성되어 있다.  

함수를 async를 붙이라니까  
`async def fetcher(session, url):` 를 붙여서 코루틴으로 만들어준다.  

<br>

`html = await response.text()` 자체가 awaitable 메서드로 보인다.  
async 키워드를 해당하는 컨텍스트에서도 적용을 해줘야한다고 한다.  

<br>

fetcher 함수를 아래와 같이 수정했다.

<br>

```
async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()
```

<br>

이제 main 함수를 수정하자.  

`with aiohttp.ClientSession() as session:`도 async 를 붙여주라고 한다.  

<br>

```
async with aiohttp.ClientSession() as session:
    result = await fetcher()
    print()
```

<br>

fetcher() 함수는 코루틴 함수이기 때문에 awaitable 객체이기 때문에 객체 형태로 받아야한다.  

`result = await asyncio.gather(*[fetcher(session, url) for url in urls])`

코드를 언팩킹 `*` 시켜준다.  
언팩킹된 원소가 쉼표 단위로 넘겨주게 된다.  
그럼 asyncio.gather 메서드를 통해 동시성 프로그래밍하게 된다.

<br>

메인 루틴도 수정한다.

asyncio는 서브 루틴을 실행시키려면 run 명령어를 사용해야한다.

```
asyncio.run(main())
```



```
import aiohttp
import time
import asyncio


async def fetcher(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = ["https://naver.com", "https://google.com", "https://instagram.com"] * 10

    async with aiohttp.ClientSession() as session:
        result = await asyncio.gather(*[fetcher(session, url) for url in urls])
        print(result)


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)
```

<br>

처음에 살짝 블로킹이 걸렸지만 실행 속도가 장난이 아니다.  
10배 이상 빠른 것을 확인할 수 있다.

코루틴 안쓴것

```
12.276936292648315
```

<br>

코루틴 쓴 것

```
1.662308931350708
```