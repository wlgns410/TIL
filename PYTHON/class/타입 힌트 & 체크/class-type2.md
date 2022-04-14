# 클래스 타입
클래스 안에서 자기 자신을 참조할 때, 사용되는 패턴이 있다.  
또한 optional 과 클래스가 만났을 때도 사용되는 패턴이 있다.  
이를 알아보자.


<br>

이전에는 instance에 클래스 이름을 넣어서 테스트를 했었다. 근데 클래스 이름에 ""를 붙여도 정상적으로 실행된다.  

`"Hello"` 처럼 사용해봤다.  

<br>

```
class Hello:
    def world(self) -> int:
        return 7

class say:
    pass

hello: Hello = Hello()

def foo(instance: "Hello") -> int:
    return instance.world()

print(foo(hello))
```

```
Success: no issues found in 1 source file
7
```

<br>

# 자기 자신을 생성자에 넣어야하는 경우

이 경우에는 class 가 선언이 안되어 있다. 그럼 어떻게 사용할 수 있을까?

```
class Node:
    def __init__(self, data: int, node: "Node"):
        self,data = data
        self.node = node

node = Node(12)
```

<br>

우선 `node: "Node"` 에서 Node는 선언이 안되어있으므로 ""를 감싸준다.  
근데 문제는 `node = Node(12)`이다.  
파라미터 개수가 부족하기 때문이다.  

<br>

이때 Optional type을 사용한다.  
Optional은 타입이 될 경우와  None이 될 경우에 사용한다.

<br>

```
from typing import Optional

class Node:
    def __init__(self, node: Optional["Node"] = None):
        self.node = node

node2= Node(None)
```

```
Success: no issues found in 1 source file
```

<br>

위 경우에는 `Union["Node", None] 과 Optional["Node"] `이 같은 것이다.

<br>

또는 python에서 지원해주는 default값을 명시해주는 방법도 있다.

```
class Node:
    def __init__(self, node: "Node" = None) -> None:
        self.node = node

node2= Node()
```

```
Success: no issues found in 1 source file
```

# 요약
타입이 존재하는 언어에서는 Optional, Union 타입을 명시해주는 것이 좋겠다.  
하지만, 파이썬의 경우에는 None default 값을 주는 것이 더 나을 수도 있어 보인다.  
파이썬의 타이핑은 결국 타입 힌트에 불과하기 때문이다.  
결국은 코드 컨벤션에 달린 것 같다.  