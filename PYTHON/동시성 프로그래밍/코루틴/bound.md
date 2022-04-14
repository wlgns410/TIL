# CPU bound, IO bound

- cpu bound : 프로그램이 실행될 때 실행속도가 cpu 속도에 의해 제한된다는 것. - > 연산 o
- io bound : 사용자의 요청 (input과 output)에 의해 실행속도가 제한된다는 것. -> 연산 x


<br>

# python i/o bound 

io_bound_func()을 요청을 보낸다. 그럼 응답까지 기다려준다. 이 과정에서 cpu는 연산을 하지않는다.  
응답이 오고 요청을 보내고 반복까지 시간이 걸린다.  
이것을 i/o 바운드라고 한다.  

<br>

```
import requests

def io_bound_func():
    result = requests.get("https://google.com")
    return result

if __name__ == "__main__":
    for i in range(20):
        result = io_bound_func()
        print(result)
```

```
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>
<Response [200]>

[Done] exited with code=0 in 11.148 seconds
```

<br>

바운드에 의해 코드가 멈추게되는 현상이 일어났다. 이것을 `블로킹`이라고 한다.  
나는 바운드에 의해 20번 코드가 멈췄다. -> 20번 호출을 했기 때문

<br>

<br>

그럼 burst를 알아보자.

<br>

> 어떤 특정된 기준(criterion)에 따라 한 단위로서 취급되는 연속된 신호(signal) 또는 데이터의 모임. 어떤 현상이 짧은 시간에 집중적으로 일어나는 현상. 또는 주기억 장치의 내용을 캐시 기억 장치에 블록 단위로 한꺼번에 전송하는 것.

<br>

- cpu burst : 프로세스 내에서 cpu 작업이 연속된 상태
- io burst : 로컬 혹은 네트워크 등의 i/o wait 작업이 연속된 상태

<br>

