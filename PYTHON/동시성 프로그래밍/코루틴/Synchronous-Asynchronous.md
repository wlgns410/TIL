# 동기와 비동기

- 동기 : 코드가 작성된 순서대로 실행된다.
- 비동기 : 코드가 작성된 순서대로 실행되는 것이 아니다.

<br>

# 동기 예시

<br>

```
import time #  epoch time(Unix time, POSIX time)을 다룰때 사용.

def delivery(name, mealtime):
    print(f"{name}에게 배달 완료하였습니다.")
    time.sleep(mealtime)

    print(f"{name} 식사 완료, {mealtime}시간 소요")
    print(f"{name}님 주소로 그릇 수거를 완료하였습니다.")

def main():
    delivery("A", 3)
    delivery("B", 4)
    delivery("C", 5)


if __name__ == "__main__":
    start = time.time()
    print("start :", start)
    main() # main이 다 수행이 되고

    end = time.time()
    print("end :", end)
    print(end - start) # 메인이 다 수행되고 나서 총 수행시간을 출력
```

```
start : 1649912827.253529
A에게 배달 완료하였습니다.
A 식사 완료, 3시간 소요
A님 주소로 그릇 수거를 완료하였습니다.
B에게 배달 완료하였습니다.
B 식사 완료, 4시간 소요
B님 주소로 그릇 수거를 완료하였습니다.
C에게 배달 완료하였습니다.
C 식사 완료, 5시간 소요
C님 주소로 그릇 수거를 완료하였습니다.
end : 1649912839.265068
12.011538982391357
```

<br>

# 비동기 예시

<br>

```
import time, asyncio

async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료하였습니다.")
    await asyncio.sleep(mealtime)

    print(f"{name} 식사 완료, {mealtime}시간 소요")
    print(f"{name}님 주소로 그릇 수거를 완료하였습니다.")


async def main():
    await asyncio.gather(
        delivery("A", 20),
        delivery("B", 4),
        delivery("C", 5),
    )

if __name__ == "__main__":
    start = time.time()
    print("start :", start)
    asyncio.run(main())

    end = time.time()
    print("end :", end)
    print(end - start)
```

```
start : 1649913238.275244
A에게 배달 완료하였습니다.
B에게 배달 완료하였습니다.
C에게 배달 완료하였습니다.
B 식사 완료, 4시간 소요
B님 주소로 그릇 수거를 완료하였습니다.
C 식사 완료, 5시간 소요
C님 주소로 그릇 수거를 완료하였습니다.
A 식사 완료, 20시간 소요
A님 주소로 그릇 수거를 완료하였습니다.
end : 1649913258.2807848
20.00554084777832
```

<br>

A가 20초가 걸리니까 B -> C -> A 순서대로 끝났다.  

<br>

동기는 네트워크 io와 비슷하다.  
음식 배달 요청을 보냈다(delivery()) -> I  
먹을 때까지 기다린다(응답) -> O  
이 요청과 응답을 반복한다  

<br>

비동기는 조금 다른데  
음식 배달 요청을 보냈다(delivery(A)) -> I  
음식 배달 요청을 보냈다(delivery(B)) -> I  
음식 배달 요청을 보냈다(delivery(C)) -> I 이렇게 다른 함수로 넘어간다.  

<br>

음식 배달 응답을 받는다(delivery(B)) -> O  
음식 배달 응답을 받는다(delivery(C)) -> O  
음식 배달 응답을 받는다(delivery(A)) -> O  

<br>

`동시에 처리한다`라는 의미에서 동시성 프로그래밍이라고 한다.

<br>

await은 비동기 함수를 처리할 때 사용하는 키워드로 단순히 동기 -> 비동기로 넘어가는데 사용되는 메서드에 그치는 것이 아니다.  
await을 기점으로 다른 코루틴으로 넘어간다.  
아래처럼 main 함수를 작성하면 delivery 코루틴으로 넘어가서 동기적으로 코드가 작동한다.  

<br>

```
import time, asyncio

async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료하였습니다.")
    await asyncio.sleep(mealtime)

    print(f"{name} 식사 완료, {mealtime}시간 소요")
    print(f"{name}님 주소로 그릇 수거를 완료하였습니다.")


async def main():
    await delivery("A", 20)
    await delivery("B", 4)
    await delivery("C", 5)

if __name__ == "__main__":
    start = time.time()
    print("start :", start)
    asyncio.run(main())

    end = time.time()
    print("end :", end)
    print(end - start)
```