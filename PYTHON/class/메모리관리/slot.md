# 객체의 메모리를 효율적으로 관리하는 방법

- 객체 내에 있는 변수들은 __dict__ 를 통해서 관리가 된다.
- __slots__를 통해 변수를 관리
- 파이썬 인터프리터에게 통보, 해당 클래스가 가지는 속성을 제한한다.
- __dict__를 통해 관리되는 객체의 성능을 최적화한다. -> 다수의 객체 생성 시 메모리 사용 공간을 대폭 감소한다.


<br>

`slot`이 없는 보통의 객체는 `__dict__`를 통해 관리가 된다.(dict 타입으로 관리된다.)

<br>

```
class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name


wos = WithoutSlotClass("지훈", 28)

print(wos.__dict__)

wos.__dict__['hello'] = 'world'

print(wos.__dict__)
```

<br>

```
{'name': '지훈'}
{'name': '지훈', 'hello': 'world'}
```

<br>

객체가 가진 속성을 제한한다면(필요한 속성만 제한한다면) 성능이 증가하게 될 것.

<br>

```
class WithSlotClass:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


slotsss = WithSlotClass('이지훈', 29)

print(slotsss.__dict__)
print(slotsss.__slots__)
```

```
Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/slot.py", line 25, in <module>
    print(slotsss.__dict__)
AttributeError: 'WithSlotClass' object has no attribute '__dict__'
```

<br>

즉, `WithSlotClass` 는 dict로 관리하는 것이 아닌, 리스트 형태로 관리하게 된다.  
또한 name, age 속성만 사용할 수 있도록 제한을 걸었다.  
이럼 메모리 전략이 되는 것이다.


<br>

### 메모리 사용량 비교
slot을 사용한 것과 사용하지 않은 것의 성능을 비교해보자.


<br>

```

import timeit

# 슬롯 없음
class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name

wos = WithoutSlotClass("지훈", 28)




# 슬롯 있음
class WithSlotClass:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

slotsss = WithSlotClass('이지훈', 29)


def repeat(obj):
    def inner():
        obj.name = "메시"
        obj.age = 11
        del obj.name
        del obj.age

    return inner


use_slot_time = timeit.repeat(repeat(slotsss), number=99999)
no_slot_time = timeit.repeat(repeat(wos), number=99999)

print("use slot : ", min(use_slot_time))
print("no slot : ", min(no_slot_time))
```

<br>

```
use slot :  0.024403305000000014
no slot :  0.032201372000000006
```

<br>

slot을 사용할 때가 효율이 더 좋다는 것을 알게되었다.
무작정 쓰는 것은 좋지 못하다. 필요한 부분만 수정하면서 사용하면 되는데, 이 과정을 리팩토링이라고 한다.  

<br>