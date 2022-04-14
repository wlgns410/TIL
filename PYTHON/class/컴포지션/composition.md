# 컴포지션

- 다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않은 경우
- 부모 클래스가 변하면 자식 클래스는 계속 수정되어야 한다.
- 부모 클래스의 메서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류 가능성이 증가하게 되므로 컴포지션이 좋은 방법이 될 수 있다.


<br>

```

class Robot(object):

    __population = 0

    def __init__(self, name, age):
        self.__name = name 
        self.__age = age
        Robot.__population += 1 

    #  인스턴스 메서드
    def cal_add(self, a, b):
        return a + b + 1


class Siri(Robot):
    def say_apple(self):
        print("apple")

    
class SiriKo(Robot):
    def say_apple(self):
        print("사과")


class Bixby(Robot):
    def say_bixby(self):
        print("빅스비!")


```

<br>

위와 같은 코드가 있다고 생각해보자. 만약 급하게 코드를 수정해야한다. 근데, `cal_add` 메서드의 내부 코드가 엄청나게 복잡한 코드라서  
이해하기 어렵다고 생각해본다면, 코드를 어떻게 수정해야할까? -> 컴포지션을 적용해본다.

<br>

```
class BixbyCal:
    def __init__(self, name, age):
        self.Robot = Robot(name, age)

    def cal_add(self, a , b):
        return self.Robot.cal_add(a, b)
```

<br>

기존의 상속 개념에서의 자식클래스가 부모클래스의 모든 속성을 물려받는게 아니라, 자식클래스가 필요한 속성만 부모클래스로부터 가져와 사용하는 것으로 코드를 수정할 수 있다.
아래와 같이 사용가능한 메서드를 보면 `cal_add`만 가져왔고, 나머지 메서드는 없는 것을 볼 수 있다.

```
print(dir(Robot))
print(dir(BixbyCal))

['_Robot__population', '_Robot__say_hi', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'cal_add', 'how_many', 'name']


['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'cal_add']
```

<br>

요약하자면, 상속과 컴포지션은 단순히 별개의 것이 아니라 비슷한 것처럼 보인다.  
기존의 클래스를 재사용하는 상황에 있어서, 상속을 사용해야 할지 컴포지션을 사용해야 할 지 어려워 보이는 것은 당연하다.  
단순히 현상황만을 고려한다기 보다는 상속과 컴포지션의 특징 및 장단점을 잘 생각하고 활용해야 새롭게 정의하는 클래스가 추후 가져올 문제를 최소화 할 수 있을 것 같다.
