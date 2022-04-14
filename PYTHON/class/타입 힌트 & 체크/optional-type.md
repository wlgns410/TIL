# optional type
타입을 명시할 때 None이 등장할 수 있다. optional type은  None이 허용되는 함수의 매개 변수에 대한 타입을 명시하는데 좋다.  
요약하자면, 있을 수도 있고 없을 수도 있는 타입에 대해서 명명하는 것으로 Union 타입과 비슷하다.

<br>

union 타입으로 작성

```
from typing import Union

xxx: Union[str, None] = "이지훈"

xxx = None
```

<br>

optional type으로 작성

```
from typing import Optional

xxx: Optional[str] = "이지훈"

xxx = None
```

<br>

# 예시
callable 객체가 None일 수도 있고, 다른 type일 수도 있을 때

```
from typing import Union, Optional

def foo(name: str) -> Optional[str]:
    if name == "이지훈":
        return None
    else:
        return name

print(foo("이지훈"))
```

```
Success: no issues found in 1 source file
None
```