## 상속(inheritance)
부모 Class의 속성값과 행위(methods)을 그대로 상속 받고 행위(methods)의 일부분을 수정해야 할 경우 상속받은 자식 Class에서 해당 행위(methods)만 다시 수정하여 사용할 수 있도록 한다.  
또한 자식 Class에서 추가적으로 속성값이나 행위(methods)를 정의할 수 있게 한다.

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩  
4. Super( ) 
5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것은 객체이다. -> object.md
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

    @classmethod
    def how_many(cls): #cls 는 클래스를 받음 -> 여기서는 cls = Robot 이 됨
        print(f"we have {cls.population} yyyyyyes")


## 클래스 상속
class Siri(Robot):

    def call_me(self):
        print("응")

    def cal_mul(self, a, b):
        self.a = a # a에 대한 속성
        return a * b

```



### mro() 메서드
`mro()`는 상속의 관계(순서)를 알려주는 메서드이다.

<br>

```
siri = Siri("iphon8")
print(Siri.mro())
print(Robot.mro())
```

#### 결과

<br>

```
[<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]
[<class '__main__.Robot'>, <class 'object'>]
```

<br>

위를 보면 궁금증이 생긴다. `class Robot` 은 부모 클래스라 아무 상속도 받지 않는데, `object`라고 뜨고 있다.

<br>

사실 `class Robot(object):`에서 `object`를 생략한 것이다.

#### 테스트

<br>

```
class Robot(object):
    ...


siri = Siri('iphone8')

print(Siri.mro())
print(Robot.mro())

```

#### 결과

<br>

```
[<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]
[<class '__main__.Robot'>, <class 'object'>]
```

<br>

똑같이 나오는 것을 확인할 수 있다.


#### object란 무엇일까?
테스트를 한 번 해보자.

<br>

```
class Robot(object):
    ...


print(object)

print(dir(object)) # 속성값
print(object.__name__) # __str__ 

print(int.mro())

```

<br>

#### 결과

<br>

```
<class 'object'>
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
object
[<class 'int'>, <class 'object'>]
```

<br>

`int`를 봐도 object를 상속을 받은 int에 대한 인스턴스라는 것을 알 수 있다.
즉, 파이썬에서 제공해주는 모든 것은 애초에 객체 상태인 것이고, `class ....` 이라고 작성하는 것은 내가 추가적으로 작성하고 있는 것이었다.

<br>
<br>

### 다중상속

<br>

```
class A:
    pass

class B:
    pass

class C:
    pass

class D(A, B, C):
    pass


```

<br>

```
print(D.mro())

[<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

```

<br>

`class D`와 같이 여러개의 클래스를 상속받는 것을 다중상속이라고 한다.
하지만 이렇게 사용하는 것은 안티패턴으로 추천하지않는다고 한다.
믹스인이라는 클래스를 사용할 때는 다중상속으로 사용하는데, 의미없는 상속의 경우에는 안티패턴을 유발한다.
순서를 예측하기 어려운 경우에서 다중 상속을 쓰면 유지보수가 어렵기 때문이다.
하지만 모든 것을 부품화처럼 잘게 쪼개고 합치는 데에는 유용하다.
