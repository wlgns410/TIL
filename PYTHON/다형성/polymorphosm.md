# 다형성

- 여러 형태를 가질 수 있도록 한다.(부품화)
- 같은 형태의 코드가 다른 동작을 할 수 있게 만드는 것


<br>

```
class Robot(object):
    ...


class Siri(Robot):
    def say_apple(self):
        print("apple")

    
class SiriKo(Robot):
    def say_apple(self):
        print("사과")


class Bixby(Robot):
    def say_bixby(self):
        print("bixby!")


class BixbyKo(Robot):
    def say_bixby(self):
        print("빅스비!")

```

<br>

다형성이란 같은 형태의 코드가 다른 의미를 가지게 하는 것이 다형성을 가진 코드를 의미한다.
다형성을 가지는 코드는 재사용성 및 유지보수가 수월하다.
