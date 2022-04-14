# 큐 자료구조
큐는 선입 선출 구조로 가장 먼저 들어온 데이터가 가장 먼저 빠져나가는 구조이다.  

<br>

스택과 코드는 똑같으며, 클래스 상속을 받아서 빼는 부분만 코드를 수정하면 된다.


<br>

# queue 구현

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


class Queue(LinkedList[T], Generic[T]):
    def enqueue(self, item: T) -> None:

        new_node: Node[T] = Node[T](item=item)
        if self.head is None:
            self.head = new_node
            return 

        # 여러번 푸쉬를 해서 노드가 여러개 생겼을 경우
        current_node = self.head
        while current_node.pointer is not None: # pointer 가 None일때까지 돌리는 것
            current_node = current_node.pointer

        current_node.pointer = new_node # 맨 마지막에 와서 새로운 노드를 넣어주면, 마지막에 노드를 넣는 것이 됨

    # 큐는 맨앞에 있는 것 제거시켜주면 됨
    def dequeue(self) -> T:
        if self.head is None:
            raise ValueError("queue is empty")
        current_node = self.head

        #  현재 노드가 첫번째라면
        if current_node.pointer is None:
            self.head = None
            return current_node.item

        result = current_node.item
        self.head = current_node.pointer
        return result

# 유닛테스트
if __name__ == "__main__":
    queue = Queue[int]()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    queue.dequeue() # 앞에 있는 1이 빠져나가는 것

    print(queue.length)
    print(queue)

```

```
count :  3
None
2, 3, 4
```