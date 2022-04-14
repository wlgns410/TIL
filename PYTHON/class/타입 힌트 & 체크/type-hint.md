# 파이썬 타입 힌트
파이썬은 타입 힌팅을 통해 데이터의 타입을 유추할 수 있다.

<br>

```
from typing import List, Tuple, Dict

int_var: str = 88
list_var : List[int] = [1,2,3]
list_var : List[str] = ["1","2","3"]
tuple_var : Tuple[int] = (1,2,3)
dict_var : Dict[str, int] = {"hello":47}
```

<br>

보통의 경우 : int, str, None 등을 사용하지만, list나 dict, tuple의 경우 안의 데이터까지 type을 알려줄 수 있다.

<br>

특정 타입에 대한 계산이 진행될 경우에 type을 지정하지 않으면, 협업 시 함수나 클래스의 기능을 잃을 수 있다.

<br>

```
def cal_add(x, y):
    return x + y

print(cal_add(1, 3))

cal_add("1, ", "이지훈")
```

<br>

만약 내가 cal_add 함수를 int 끼리 더하는 함수로 작성했다 할지라도, 다른 개발자는 str끼리 결합하는 문자열로 인식해서 함수를 사용할 수 있다.
그럼 이 함수의 목적은 상실된 것이다.  
이런 문제를 해결하려면 type을 알려주면 된다.  

<br>

```
def cal_add(x: int, y:int) -> int:
    return x + y


print(cal_add("1", 2))
```

```
Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/type.py", line 22, in <module>
    print(cal_add("1", 2))
  File "/Users/jihoon/project/python-class/type.py", line 19, in cal_add
    return x + y
TypeError: can only concatenate str (not "int") to str
```

<br>

다음과 같이 에러가 나는 것을 알 수 있다.

<br>

# 타입 체크
`isinstance(obj, class)` 이 오브젝트가 class에 대한 인스턴스 인지 확인해준다.  
여기에 type_check 함수를 같이 사용해주면 좋다.  


<br>

```
from typing import Any # Any는 아무거나 들어가도 된다라는 뜻이라 파이썬에서는 암묵적으로 기재하지 않는다고 한다.

def type_check(obj: Any, typer) -> None:

    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"type error : {typer}")

def cal_add(x: int, y:int) -> int:

    type_check(x, int)
    type_check(y, int)
    return x + y

print(cal_add(1, 3))
```

<br>

하지만 모든 함수에 타입 힌트를 적으면 생산성이 감소될 수 있으므로 중요한 함수에만 기재하는 등 개발자들끼리 약속을 한다고 한다.  

<br>