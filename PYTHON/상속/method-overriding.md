## 상속(inheritance)
부모 Class의 속성값과 행위(methods)을 그대로 상속 받고 행위(methods)의 일부분을 수정해야 할 경우 상속받은 자식 Class에서 해당 행위(methods)만 다시 수정하여 사용할 수 있도록 한다.  
또한 자식 Class에서 추가적으로 속성값이나 행위(methods)를 정의할 수 있게 한다.

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩  -> method-overriding.md
4. Super( )
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

siri = Siri('iphone8')
siri.call_me()

print(siri.cal_mul(7, 8))

Siri.hello_apple() # 클래스 메서드이기 때문에 siri.hello_apple() 보다는 Siri.hello_apple() 호출이 맞음

```

### 메서드 오버라이드
부모 클래스에서 이미 `def __init__(self, name):`로 생성자를 작성했다.
근데 자식 클래스에서 다시 한번 `__init__`으로 초기화를 한다면 어떻게 될까? -> 메서드 오버라이딩이 된다.

<br>

```
class Siri(Robot):
    def __init__(self, name, age):
            self.name = name 
            self.age = age
            Siri.population += 1 

    @classmethod
    def how_many(cls):
        return f'we have {cls.population} by apple'

```

#### 결과
```
we have 1 by apple
```

이렇게 호출을 해도 되는 이유가 `population`이라는 변수가 Robot이라는 부모 클래스에 존재하기 때문에  
사용할 수 있게 되기 때문.