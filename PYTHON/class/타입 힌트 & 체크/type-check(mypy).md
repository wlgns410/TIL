# 타입 체크 2

<br>

`type-hint.md` 다음 블로깅입니다. 

<br>
파이썬에는 타입 체크를 도와주는 라이브러리가 있다.


> pip install mypy


<br>

라이르러리를 설치하고 원하는 스크립트를 실행한다.

<br>

> mypy type.py

```
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
성공시

<br>

```
Success: no issues found in 1 source file
```

<br>

실패시

<br>


```
type.py:40: error: Argument 2 to "cal_add" has incompatible type "str"; expected "int"
Found 1 error in 1 file (checked 1 source file)
```

<br>

`mypy` 라이브러리는 타입 체킹만 해주고 결과값을 알려주지는 않는다는 단점이 있다.  
> mypy type.py && python type.py 

<br>

```
Success: no issues found in 1 source file
4
```

<br>

다음과 같이 결과값도 같이 알 수 있다.