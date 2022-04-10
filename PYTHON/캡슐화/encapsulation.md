# 캡슐화 (encapsulation)
객체(object)의 속성과 행위(method)를 하나로 묶고, 구현된 일부를 감추어 은닉한다.



```
class Robot:

    """
    # 이름 : 이지훈
    # 코드 : 무야호
    """

    # 인스턴스들이 공유하는 변수를 생성
    population = 0

    # 생성자는 인자를 받아서 인스턴스에 붙여넣어주는 역할
    def __init__(self, name, age):
        self.name = name # name : 키, siri : 밸류 로 저장이 되는 것
        self.age = age
        Robot.population += 1 # Robot을 호출하면 1개씩 증가하게

    #  인스턴스 메서드
    def say_hi(self):
        print("greetings")

    #  인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls): #cls 는 클래스를 받음 -> 여기서는 cls = Robot 이 됨
        print(f"we have {cls.population} yyyyyyes")

```

### private 메서드
파이썬에는 객체의 속성을 지정해서 함부러 접근할 수 없게 만들 수도 있다.

위 같은 코드에서 아래처럼 바꿔본다.

<br>

```
def __init__(self, name, age):
        self.name = name # name : 키, siri : 밸류 로 저장이 되는 것
        self.__age = age
        Robot.population += 1 # Robot을 호출하면 1개씩 증가하게

ss = Robot("지훈", 28)
print(ss.age)

ss.age = -33

print(ss.age)
```

<br>

#### 결과

<br>

```
Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/encapusulation.py", line 31, in <module>
    print(ss.age)
AttributeError: 'Robot' object has no attribute 'age'
```

<br>

위와 같이 age에 접근할 수 없을 것이다.
파이썬에서는 `__` 언더바 2개를 쓰면 private 메서드가 된다.

<br>
그럼 `__age`는 접근할 수 있을까?

<br>

```
print(ss.__age)

Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/encapusulation.py", line 35, in <module>
    print(ss.__age)
AttributeError: 'Robot' object has no attribute '__age'
```

<br>

이것도 접근을 할 수 없다.
이건 왜 접근할 수 없을까? -> private 메서드 때문에 접근이 불가하다.


### public 메서드
public 메서드는 앞 뒤로 `__` 언더바를 써주면 된다.

<br>

```
def __init__(self, name, age):
        self.name = name 
        self.__age__ = age
        Robot.population += 1 


ss = Robot("지훈", 28)

print(ss.__age__)
```

```
28
```

<br>

결과가 나오는 것을 알 수 있다. 이런걸 private와 public 메서드이다. 하지만 이렇게 코딩하지않는다.
암묵적으로 개발자들끼리 맞추는 편이라고 한다.

<br>

### public protect, private
protect는 상속을 받았을 때, 상속한 대상한테까지는 알려주지만, 외부로는 알려주지 않는 것이다.

<br>

```
class Robot(object):
    population = 0

    def __init__(self, name, age):
        self.name = name 
        self.__age = age
        Robot.population += 1 


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        print(self.__age)
        self.__age = 999


ss = Robot("지훈", 28)

ssss = Siri("iphone", 10)
```

<br>

호출을 해보면 에러가 뜬다. `self.__age = 999`를 호출했을 때 새롭게 private 변수로 들어가버린 것이다.

<br>

```
Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/encapusulation.py", line 40, in <module>
    ssss = Siri("iphone", 10)
  File "/Users/jihoon/project/python-class/encapusulation.py", line 33, in __init__
    print(self.__age)
AttributeError: 'Siri' object has no attribute '_Siri__age'
```

<br>

그럼 호출 순서를 바꿔보도록 하자.

<br>

```
class Robot(object):
    population = 0

    def __init__(self, name, age):
        self.name = name 
        self.__age = age
        Robot.population += 1 


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)
        
        self.__age = 999
        print(self.__age)


ss = Robot("지훈", 28)

ssss = Siri("iphone", 10)
```

<br>

```
999
```

<br>

결과가 호출이 된다.  
부모 클래스인 Robot에서 `self.__age = age`가 은닉이 되었기 때문에 없는 변수라고 생각하고  
자식 클래스인 Siri에서 `self.__age = 999`를 호출하게 되는데, 부모 클래스의 `self.__age = age` 속성 자체가 네임 스페이스에 감춰지기 때문이다.
* 타입 스크립트는 protect처럼 작성해도 접근할 수 있다고 하지만, 파이썬은 직접적으로는 protect를 제공하지 않는다고 본다.

<br>


### 클래스 메서드에도 적용이 될까?
다음과 같이 적어봤다.


<br>

```
class Robot(object):
    def __say_hi(self):
            print("greetings")



ss = Robot("지훈", 28)
ss.__say_hi()
```

<br>

```
Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/encapusulation.py", line 43, in <module>
    ss.__say_hi()
AttributeError: 'Robot' object has no attribute '__say_hi'
```

<br>

`__`을 붙이면 변수, 함수, 메서드 다 은닉화가 되서 호출을 할 수 있게 된다.

<br>