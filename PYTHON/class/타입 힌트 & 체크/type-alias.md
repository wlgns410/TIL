# type alias

타입에 붙일 수 있는 별칭을 말한다.  
typealias는 새로운 타입을 만드는 것이 아니라 기존 이름을 새로운 별칭으로 호출할 수 있는 것이다. 

<br>

예를 들어 복잡한 구조의 타입 힌팅이 있다고 가정한다.

```
from typing import Union, List, Tuple, Dict, Optional

value: Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]]= 1

def cal(v:  Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]
]) ->  Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]
]:
    return v
```

<br>

변수처럼 사용해주면 된다.  
이걸 type alias라고 부른다.

```
Value = Union[int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]]

value: Value = 1

def cal(v: Value) -> Value:
    return v
```

# 예시

쉬운 예시를 들어보자.

```
X = int
x: X = 8
 
print(x)
```

```
Success: no issues found in 1 source file
8
```


<br>
<br>

# dictionary alias

딕셔너리에도 타입을 지정할 수 있다.

```
ddd: Dict[str, str] = {"hi":"jihoon"}
```

```
Success: no issues found in 1 source file
```

# 예시
성공 예시

<br>

```
from typing_extensions import TypedDict

class Di(TypedDict):
    name: str
    age: int
    height: float


di: Di = {"name": "지훈", "age":28, "height":176.3,}
```

```
Success: no issues found in 1 source file
```

<br>

실패예시

<br>

```
class Di(TypedDict):
    name: str
    age: int
    height: float


di: Di = {"name": "지훈", "age":28, "height":176.3, "hi":"hi"}
```

```
type.py:171: error: Extra key "hi" for TypedDict "Di"
Found 1 error in 1 file (checked 1 source file)
```