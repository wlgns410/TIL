# 스택 자료구조
스택은 데이터의 삽입과 삭제가 가장 마지막에 삽인된 데이터부터 적용되는 것을 말한다.  
이를 LIFO(후입선출)이라고 한다.  

<br>

데이터를 삽입하는 과정을 push, 마지막에 삽입한 데이터를 삭제하는 과정을 pop이라고 부른다.  
데이터를 삭제하는 pop의 경우 현재 스택에서 데이터가 비어있는 지 여부를 판단하고 나서야 pop이 동작한다.  

<br>

append는 stack의 가장 마지막에 데이터를 추가하는 메서드이다.
pop은 가장 마지막에 삽입한 데이터를 삭제하는 메서드이다.
top은 가장 마지막에 삽입한 데이터를 삭제하지 않고 return을 하는 메소드이다.
isempty는 스택이 비어있는지 여부를 판단하는 메서드이다.

<br>


파이썬은 list의 append, pop을 통해 스택을 구현할 수 있다.  
하지만, class를 통해 구현을 해보자.

<br>

`Node Class` 작성
- item
- pointer : 다음 node를 가리키므로 다음 node를 저장하고 아무것도 가리키지 않으면 None을 저장한다.

<br>

`LinkedList class`
- head : 가장 첫 번째 node, node가 없으면 None을 저장한다.
- length : int 타입, 현재 노드(데이터)의 개수를 의미한다.

<br>

`Stack class` : LinkedList를 상속받는다.
- push(item) : Stack 자료구조에 item을 받아 노드로 만든 다음 밀어넣는다.
- pop() : Stack 자료구조에서 마지막 node를 제거하고 해당 Item을 반환한다.

<br>

```
from typing import Optional


class Node:
    def __init__(self, item, pointer: Optional["Node"] = None):
        self.item = item
        self.pointer = pointer


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None # 초기값이 None이므로 head는 맨 앞을 위미

    @property # 의미론적으로 속성 느낌이라 property 붙임
    def length(self):
        if self.head is None: # 애초에 아무것도 존재하지 않을 때
            return 0

        pass


class Stack(LinkedList):

    # 자식 클래스가 부모 클래스를 상속받았으니, 생성자를 또 생성할 필요가 없음
    # def __init__(self):

    def push(self, item) -> None:
        new_node: Node = Node(item=item)
        if self.head is None:
            self.head = new_node
            return 

        # 여러번 푸쉬를 해서 노드가 여러개 생겼을 경우
        current_node = self.head
        while current_node.pointer is not None: # pointer 가 None일때까지 돌리는 것
            current_node = current_node.pointer

        current_node.pointer = new_node # 맨 마지막에 와서 새로운 노드를 넣어주면, 마지막에 노드를 넣는 것이 됨


# 유닛테스트
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)

    print(stack.head)

    print(stack.head.item)
```

<br>

> `if __name__ == "__main__"` 경우, 조건문을 사용하여 터미널에서와 같이 직접 호출되어 사용될 때는 그 자체로 기능을 수행하고, 동시에 다른 모듈에서 필요한 함수 등을 제공해준다.

<br>

```
<__main__.Node object at 0x7fb57eb03eb0>
1
```


<br>

노드의 개수를 세어보자

```
class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None # 초기값이 None이므로 head는 맨 앞을 위미

    @property # 의미론적으로 속성 느낌이라 property 붙임
    def length(self):
        if self.head is None: # 애초에 아무것도 존재하지 않을 때
            return 0

        current_node: Node = self.head
        count: int = 1 # 현재 노드는 한번 셈
        while current_node.pointer is not None:
            current_node = current_node.pointer
            count += 1
        print("count : ",count)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.length)
```

```
count :  4

```

<br>

어떤 노드가 들어왔는지 read 해보자

```
def __str__(self) -> str:
        result: str = ""
        if self.head is None:
            return result
        currnet_node: Node = self.head
        result += f"{currnet_node.item}"
        
        while currnet_node.pointer is not None:
            currnet_node = currnet_node.pointer
            result += f", {currnet_node.item}"

        return result


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack)
```

```
1, 2, 3, 4
```

<br>


# pop 구현

```
def pop(self):
    # node가 1개밖에 없을 때
    if self.head is None:
        raise ValueError("stack is empty")
    else:
        current_node = self.head

    if current_node.pointer is None:
        self.head = None
        return current_node.item
    
    # 현재 노드의 포인터의 포인터가 마지막일 때
    while current_node.pointer.pointer is not None:
        current_node = current_node.pointer

    # 마지막 노드의 바로 직전
    result = current_node.pointer

    # 맨 마지막 제거
    current_node.pointer = None
    return result.item

# 유닛테스트
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print(stack.length)
    print(stack)

```

<br>

4개를 넣고 5개를 빼보자.

```
4
3
2
1
Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/stack.py", line 186, in <module>
    print(stack.pop())
  File "/Users/jihoon/project/python-class/stack.py", line 154, in pop
    raise ValueError("stack is empty")
ValueError: stack is empty
```

<br>

# generic 추가

```

from typing import Optional, Generic, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, item: T, pointer: Optional["Node"] = None):
        self.item = item
        self.pointer = pointer


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Optional[Node[T]] = None # 초기값이 None이므로 head는 맨 앞을 위미

    @property # 의미론적으로 속성 느낌이라 property 붙임
    def length(self) -> int:
        if self.head is None: # 애초에 아무것도 존재하지 않을 때
            return 0

        current_node: Node[T] = self.head
        count: int = 1 # 현재 노드는 한번 셈
        while current_node.pointer is not None:
            current_node = current_node.pointer
            count += 1
        print("count : ",count)

    def __str__(self) -> str:
        result: str = ""
        if self.head is None:
            return result
        currnet_node: Node = self.head
        result += f"{currnet_node.item}"
        
        while currnet_node.pointer is not None:
            currnet_node = currnet_node.pointer
            result += f", {currnet_node.item}"

        return result




class Stack(LinkedList[T], Generic[T]):

    # 자식 클래스가 부모 클래스를 상속받았으니, 생성자를 또 생성할 필요가 없음
    # def __init__(self):

    def push(self, item: T) -> None:
        new_node: Node[T] = Node[T](item=item)
        if self.head is None:
            self.head = new_node
            return 

        # 여러번 푸쉬를 해서 노드가 여러개 생겼을 경우
        current_node = self.head
        while current_node.pointer is not None: # pointer 가 None일때까지 돌리는 것
            current_node = current_node.pointer

        current_node.pointer = new_node # 맨 마지막에 와서 새로운 노드를 넣어주면, 마지막에 노드를 넣는 것이 됨

    def pop(self) -> T:
        # node가 1개밖에 없을 때
        if self.head is None:
            raise ValueError("stack is empty")
        else:
            current_node = self.head

        if current_node.pointer is None:
            self.head = None
            return current_node.item
        
        # 현재 노드의 포인터의 포인터가 마지막일 때
        while current_node.pointer.pointer is not None:
            current_node = current_node.pointer

        # 마지막 노드의 바로 직전
        result = current_node.pointer

        # 맨 마지막 제거
        current_node.pointer = None
        return result.item


# 유닛테스트
if __name__ == "__main__":
    stack = Stack[int]()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())


    print(stack.length)
    print(stack)

```

```
4
3
2
1
Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/stack.py", line 188, in <module>
    print(stack.pop())
  File "/Users/jihoon/project/python-class/stack.py", line 156, in pop
    raise ValueError("stack is empty")
ValueError: stack is empty
```