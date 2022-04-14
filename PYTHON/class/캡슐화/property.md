# 프로퍼티
- 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
- 인스언스 변수 값에 대한 유효성 검사 및 수정



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

### property
우선 코드를 바꿔보자

<br>

```
class Robot(object):

    __population = 0

    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        Robot.__population += 1


droid = Robot('이지훈', 2)
```

이러면 은닉화가 되서 당연히 호출이 안될것이다.
호출이 되게 @property 를 추가해보자.

<br>

```
    @property
    def age(self):
        return self.__age


droid = Robot('이지훈', 2)
print(droid.age)
```

```
2
```

<br>

호출이 잘 된다.
그럼 코드를 추가해보자.

<br>

```
droid.age = 77
```

```
Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/property.py", line 42, in <module>
    droid.age = 77
AttributeError: can't set attribute
```

<br>

`getter`라는 프로퍼티를 통해 get 속성을 통해서 age는 가져올 수 있었으나(read 기능),
set은 없다고 한다.
그럼 업데이트를 하고 싶을 때 어떻게 해야할까? -> `setter`를 사용한다.

<br>

### setter 프로퍼티

<br>

```
class Robot(object):
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        print(new_age)
        self.__age = new_age

droid = Robot('이지훈', 2)
print(droid.age)

droid.age = 7
print(droid.age)
```

<br>

```
7
7
```

<br>

결과가 잘 나온다.
`droid.age = 7`에서 new_age에 어떤 것을 대입했는 지 찾는데, 7을 대입했으므로 new_age에 7이 들어간다.
class 안에서는 private 메서드를 사용할 수 있으므로 `self.__age = new_age`가 동작한다.(밖에서 은닉을 하는 것)

<br>

데이터가 변했는지 아닌지 알 수 있는 것이 `setter` 프로퍼티를 쓰는 이유이다.

```
@age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invaild age")
        else:
            self.__age = new_age

droid.age = -1
```

```
Traceback (most recent call last):
  File "/Users/jihoon/project/python-class/property.py", line 50, in <module>
    droid.age = -1
  File "/Users/jihoon/project/python-class/property.py", line 24, in age
    raise TypeError("invaild age")
TypeError: invaild age

```

<br>

만약 데이터의 형식을 바꾸고 싶을 때도 사용한다.

<br>

#### 예시 1

```
    def __init__(self, name, age):
        self.__name = name # name : 키, siri : 밸류 로 저장이 되는 것
        self.__age = age
        Robot.__population += 1 # Robot을 호출하면 1개씩 증가하게

    @property
    def name(self):
        return f"lee {self.__name}"


droid = Robot('이지훈', 2)

print(droid.name)
```

```
lee 이지훈
```

<br>

#### 예시 2

```
@age.setter
    def age(self, new_age):
        if new_age - self.__age == 1:
            self.__age = new_age
        else:
            raise ValueError("invaild")

droid = Robot('이지훈', 2)
droid.age += 1

print(droid.age)
```

```
3
```

<br>
