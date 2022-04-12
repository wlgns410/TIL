# union 타입
흔히 합집합이라고 말하며, 여러 개의 타입을 적을 수 있다는 것을 말한다.  

로직이 돌아가기 전에는 int 형으로 두고, 로직이 돌아간 후에는 str로도 받고 싶은데, 이런 경우에 사용할 수 있다.

<br>

```
xxx: int = 1
xxx = "11"
```

<br>


```
type.py:92: error: Incompatible types in assignment (expression has type "str", variable has type "int")
Found 1 error in 1 file (checked 1 source file)
```

<br>

Union을 적용해보자.

```
from typing import Union

xxx: Union[int, str] = 3
xxx = "17"
```

```
Success: no issues found in 1 source file
```

<br>

# 예시

<br>

```
rom typing import Union

xxx: Union[int, str] = 3
xxx = "17"


def foo(x: Union[int, str]) -> Union[int, str]:
    return x

print(foo(xxx))
```

```
Success: no issues found in 1 source file
17
```
