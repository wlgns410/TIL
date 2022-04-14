# 코루틴

- 루틴 : 일련의 명령(코드의 흐름)
- 메인 루틴 : 프로그램 메인 코드의 흐름
- 서브 루틴 : 보통의 함수나 메소드
- 코루틴 : 서브 루틴의 일반화된 형태로 다양한 진입점과 다양한 탈출점이 있다.

<br>

동기-비동기.md 참고

<br>

아래와 같이 작동하는 main이 되는 코드 흐름을 메인 루틴이라고 한다.

```
if __name__ == "__main__":
    start = time.time()
    print("start :", start)
    asyncio.run(main())

    end = time.time()
    print("end :", end)
    print(end - start)
```

<br>

메인 루틴을 제외한 모든 것을 서브 루틴이라고 한다.  
서브 루틴을 실행함으로서 안에 있는 또 다른 서브 루틴이 실행된다.  

<br>

함수는 인풋값이 있으면 리턴값이 있는 구조이다.  
하나의 진입점과 탈출점이 있는 구조이다.

```
async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료하였습니다.")
    await asyncio.sleep(mealtime)

    print(f"{name} 식사 완료, {mealtime}시간 소요")
    print(f"{name}님 주소로 그릇 수거를 완료하였습니다.")


async def main():
    await delivery("A", 20)
    await delivery("B", 4)
    await delivery("C", 5)
    return None # 보통은 return이 생략되는 예시가 많다.
```

<br>

코루틴의 예시이다.  
이 함수는 await로 탈출할 수도 있고, return으로 탈출할 수도 있다.  


```
async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료하였습니다.")
    await asyncio.sleep(mealtime)

    print(f"{name} 식사 완료, {mealtime}시간 소요")
    print(f"{name}님 주소로 그릇 수거를 완료하였습니다.")
    return None
```

# 예시

우선 async를 사용해서 메인 루틴을 호출해보자.  
`await allowed only within async function`이라고 뜬다.  
await는 코루틴 안에서 사용할 수 있다는 것이다.

```
async def hello_world():
    print("hello")


if __name__ == "__main__":
    await hello_world()
```

<br>

이걸 asyncio 모듈의 도움을 받아 메인 루틴안에서 실행할 수 있게 만들어준다.  

```
import asyncio

async def hello_world():
    print("hello")


if __name__ == "__main__":
    asyncio.run(hello_world())
```

<br>

그럼 await을 아무렇게나 붙여도 되는 걸까??  
아까 await은 기점이라고 했다. 그럼 기점이 아무곳에 있어도 되는건가? 그렇게 자유로운 것인가 궁금해진다.  

<br>

```
import asyncio

async def hello_world():
    await print("hello")
    return 1


if __name__ == "__main__":
    asyncio.run(hello_world())
```

코루틴에서 await를 사용해본다.  

```
hello
Traceback (most recent call last):
  File "/Users/jihoon/project/python/동시성/coroutine.py", line 9, in <module>
    asyncio.run(hello_world())
  File "/Users/jihoon/miniconda3/lib/python3.8/asyncio/runners.py", line 43, in run
    return loop.run_until_complete(main)
  File "/Users/jihoon/miniconda3/lib/python3.8/asyncio/base_events.py", line 616, in run_until_complete
    return future.result()
  File "/Users/jihoon/project/python/동시성/coroutine.py", line 4, in hello_world
    await print("hello")
TypeError: object NoneType can't be used in 'await' expression
```

<br>

메인 루틴은 비동기라서 호출이 되었다.  
근데, print("hello") 가 awaitable 객체가 아니기 때문에 사용할 수 없다고 한다.  
공식 문서를 봐보자.


<br>


> 우리는 객체가 await 표현식에서 사용될 수 있을 때 어웨이터블 객체라고 말합니다. 많은 asyncio API는 어웨이터블을 받아들이도록 설계되었습니다. awaitalbe 객체에는 세 가지 주요 유형이 있습니다: 코루틴, 태스크 및 퓨처.


<br>

그럼 이 코드는 어떻게 실행이 되었는가 궁금해진다.  

바로 asyncio.sleep을 통해 블로킹을 시켜줬기 때문이다.  
`asyncio.sleep(mealtime)` 도 코루틴 함수가 되는 것이다.
`await asyncio.sleep(mealtime)` 그래서 awaitalbe 객체가 될 수 있었다.  
`asyncio.sleep`을 `time.sleep`으로 바꾸면 awaitable 객체가 아니라 실행이 안된다.  


```
async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료하였습니다.")
    await asyncio.sleep(mealtime)

    print(f"{name} 식사 완료, {mealtime}시간 소요")
    print(f"{name}님 주소로 그릇 수거를 완료하였습니다.")
```

<br>

## 코루틴

- 코루틴 함수란 : async def 함수를 말함
- 코루틴 객체란 : 코루틴 함수를 호출하여 반환된 객체.

## 테스크

- 코루틴을 동시에 예약하는 데 사용

```
async def main():
    task1 = asyncio.create_task(delivery("A", 3))
    task2 = asyncio.create_task(delivery("B", 1))

    await task2
    await task1

```

이렇게 사용해도 된다.

```

async def main():
    await delivery("A", 3)
    await delivery("B", 1)

```

## 퓨처

- 최종 결과를 나타내는 awaitable 객체


## 그외

- asyncio.run : 코루틴 실행 후 반환
- asyncio.sleep : 블로킹 시킴
- asyncio.gather : 동시 실행
- asyncio.shield : 객체를 취소로부터 보호
- asyncio.wait_for : 제한 시간 내까지 기다림 

등이 있다.