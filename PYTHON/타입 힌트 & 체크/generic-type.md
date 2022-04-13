# generic type
데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술

<br>


```
from typing import Optional, Union

class Robot:
    def __init__(self, arm: Union[int, str], head: int):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호 해석하는 코드라고 가정
        bbb: Optional[Union[str, int]] = None
        pass
```

<br>

Union[int, str]를 치환할 수 있는 코드가 있으면 유지보수가 수월할 것이다.  
타입을 변수처럼 사용할 수 있게 만들 수 있다.  
`제네릭 변수`를 만든 것이다.

```
from typing import TypeVar

ARM = TypeVar("ARM")
```

<br>

아래와 같이 바꿀 수 있다.  
제네릭 변수는 전체 코드에서 공유를 하는데, 생성자(init)이 지정을 해준다.  
즉, Robot 인스턴스를 짝어낼 때 샹성자를 통해 지정을 해준다는 뜻이다.  
int가 ARM으로 들어가면 ARM은 int가 되고, str가 ARM으로 들어가면 ARM은 str이 되는 것이다.  



<br>

```
from typing import Generic, Optional, TypeVar

ARM = TypeVar("ARM")

class Robot(Generic[ARM]):
    def __init__(self, arm: ARM, head: int):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호 해석하는 코드라고 가정
        bbb: Optional[ARM] = None
        pass

robot1 = Robot[int](123, 123)

robot2 = Robot[str]("1234", 1234)

robot3 = Robot[float](12345.1, 12345)        
```

```
Success: no issues found in 1 source file
```

<br>

# 성공

```
from typing import Generic, Optional, TypeVar

ARM = TypeVar("ARM")
HEAD = TypeVar("HEAD")

class Robot(Generic[ARM, HEAD]):
    def __init__(self, arm: ARM, head: HEAD):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호 해석하는 코드라고 가정
        bbb: Optional[ARM] = None
        pass

robot1 = Robot[int, int](123, 123)

robot2 = Robot[str, int]("1234", 1234)

robot3 = Robot[float, float](12345.1, 12345.1)  
```

```
Success: no issues found in 1 source file
```

<br>

# 실패
제네릭 타입에는 어떤 타입을 받을 수 있는지도 지정할 수 있다.  
리스트 타입을 받지 않는 제네릭 변수에게 리스트를 받게 해보자.  
그럼 에러가 날 것이다.

<br>

```
from typing import Generic, Optional, TypeVar

ARM = TypeVar("ARM", int, float, str)
HEAD = TypeVar("HEAD")

class Robot(Generic[ARM, HEAD]):
    def __init__(self, arm: ARM, head: HEAD):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호 해석하는 코드라고 가정
        bbb: Optional[ARM] = None
        pass

robot1 = Robot[int, int](123, 123)

robot2 = Robot[str, int]("1234", 1234)

robot3 = Robot[list, float]([12345.1], 12345.1)        
```

```
type/generic-type.py:8: error: Need type annotation for "arm"
type/generic-type.py:20: error: Value of type variable "ARM" of "Robot" cannot be "List[Any]"
Found 2 errors in 1 file (checked 1 source file)
```

# 클래스 상속 예시

```
from typing import Generic, Optional, TypeVar, Union

ARM = TypeVar("ARM")
HEAD = TypeVar("HEAD")

class Robot(Generic[ARM, HEAD]):
    def __init__(self, arm: ARM, head: HEAD):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호 해석하는 코드라고 가정
        bbb: Optional[ARM] = None
        pass  


class Siri(Robot[ARM, HEAD], Generic[ARM, HEAD]):
    pass

siri1 = Siri[int, int](123, 123)

siri2 = Siri[str, int]("1234", 1234)

siri3 = Siri[float, float](12345.1, 12345.1)  

print(siri1.arm)
```

```
Success: no issues found in 1 source file
123
```

<br>

만약, 이렇게 클래스에서 상속을 받는다면, `cannot create consistent method ordering`에러를 볼 수 있다.

```
class Siri( Generic[ARM, HEAD], Robot[ARM, HEAD]):
    pass

```

<br>

다음과 같이 나온다.

<br>

```
print(Siri.mro())

[<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'typing.Generic'>, <class 'object'>]
```

<br>

유추하기로는 클래스 탐색순서는 MRO를 따르는데, 이 순서대로 상속을 해줘야 부모 자식간에 꼬이는 것을 방지하지 않을까 생각이 든다.

<br>

# 함수에서 사용

```
from typing import Generic, Optional, TypeVar

ARM = TypeVar("ARM")
HEAD = TypeVar("HEAD")

class Robot(Generic[ARM, HEAD]):
    def __init__(self, arm: ARM, head: HEAD):
        self.arm = arm
        self.head = head

    def decode(self):
        # 암호 해석하는 코드라고 가정
        bbb: Optional[ARM] = None
        pass

# 함수에서 사용

def test(x: ARM) -> ARM:
    print(x)
    print(type(x))
    return x

test(1)
```

```
Success: no issues found in 1 source file

<class 'int'>
```

<br>