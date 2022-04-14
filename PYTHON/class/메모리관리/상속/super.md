## 상속(inheritance)
부모 Class의 속성값과 행위(methods)을 그대로 상속 받고 행위(methods)의 일부분을 수정해야 할 경우 상속받은 자식 Class에서 해당 행위(methods)만 다시 수정하여 사용할 수 있도록 한다.  
또한 자식 Class에서 추가적으로 속성값이나 행위(methods)를 정의할 수 있게 한다.

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩  
4. Super( ) -> super.md
5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것은 객체이다.
6. mro( ) : 상속 관계를 보여준다.


```
class Robot:

    """
    # 이름 : 이지훈
    # 코드 : 무야호
    """

    # 인스턴스들이 공유하는 변수를 생성
    population = 0

    # 생성자는 인자를 받아서 인스턴스에 붙여넣어주는 역할
    def __init__(self, name):
        self.name = name # name : 키, siri : 밸류 로 저장이 되는 것
        Robot.population += 1 # Robot을 호출하면 1개씩 증가하게

    #  인스턴스 메서드
    def say_hi(self):
        print("greetings")

    #  인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    #  인스턴스 메서드
    def die(self):
        Robot.population -= 1 

        if Robot.population == 0:
            print(f"{self.name} Robot 0")
        else:
            print(f"{self.name} Robot is working")

    @classmethod
    def how_many(cls): #cls 는 클래스를 받음 -> 여기서는 cls = Robot 이 됨
        print(f"we have {cls.population} yyyyyyes")

    @staticmethod
    def are_you_robot():
        print(f"{Robot.population} 숫자는?")
        print("yest")

    # 오버라이드 되어서 self.name을 주는 것
    def __str__(self):
        return f"{self.name} robot"

    #  call 메서드를 사용했기 때문에 callable 객체가 된 것
    def __call__(self):
        print("call")
        return f"{self.name} is call!"



## 클래스 상속
class Siri(Robot):

    def __init__(self, name, age):
        self.name = name 
        self.age = age
        Siri.population += 1 

    def call_me(self):
        print("응")

    def cal_mul(self, a, b):
        self.a = a # a에 대한 속성
        return a * b

    @classmethod
    def hello_apple(cls):
        print(f'{cls} hello') # 여기서 cls는 siri를 가리킴

    def say_hi(self):
        print(f'hihihi {self.name}')

    @classmethod
    def how_many(cls):
        return f'we have {cls.population} by apple'

```

### super()
`super()`는 부모 클래스에 정의된 메서드를 사용할 수 있다.  

<br>

```
class Siri(Robot):
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        Siri.population += 1
        super().__init__()
```

`__init__`을 작성했는데, 부모의 `init`을 호출하면 어떻게 될까?

알아보기 전에, `super().__init__()`으로 인해 부모의 `__init__()`을 호출해와서 name과 population을 작성해줄 필요가 없게 된다.

<br>

```
class Siri(Robot):
    def __init__(self, name, age):
        self.age = age
        super().__init__()


siri = Siri('iphone8', 17)

print(siri.age)
print(siri.name)
```


#### 결과

<br>

```
17
iphone8
```


### 예시
만약 아래와 같이 예시가 있다고 생각하자.

<br>

```
def cal_flexable(self, a, b):
        super().say_hi() # greetings 가 호출되어야 함
        self.say_hi() # hihihi iphone8 가 호출되어야 함
        return self.cal_mul(a, b) + self.cal_add(a, b) + super().cal_add(a, b)

print(siri.cal_flexable(1, 3))
```

#### 결과

<br>

```
greetings
hihihi iphone8
11
```

<br>

`super`를 사용하면 부모의 메서드를 그대로 사용하므로 greetings 가 호출된다.
`self`를 사용하면 이미 작성해둔, 오버라이드 된 메서드를 사용하므로 hihihi iphone8 가 호출된다. -> 자식 클래스의 인스턴스를 가져옴

<br>