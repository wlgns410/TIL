# python을 이용한 딥러닝에서 객체지향 예시

보통 타 모듈을 가져와서 상속받고 부모 클래스를 작성한 뒤, 자식클래스에서 상속을 받고, 코드를 돌린다.  


<br>

```
class VGG(nn.Module):
class Machine:
class ResNetMachine(Machine):

if __name__ == "__main__":
    ...
```

<br>

클래스 내부 구조

<br>

```
class Machine:

    """
    알림
    """

    BASE_DIR = "/content/mai_drive/MyDrive/deep_learning"

    def __init__(self, batch_size: int = 64, epoch_size: int = 1):

    def get_data(self):

    @staticmethod
    def vgg16():

    def train(self, epoch):

    def test(self):

    def learning(self):

```

<br>

코드를 모른다고 가정하자.  
이렇게 돌아간다.

<br>

`"""` 안에 알려야하는 것을 기재하고  
`클래스 변수`를 지정해서 파일의 위치를 지정해서 인스턴스 내에서 공유하는 변수들을 기재하고    
`__init__` 생성자 변수를 만들어서 파라미터를 입력받고  
`def vgg16():` 모델을 만들고  
`def get_data(self):` 데이터를 가져오고  
`def train(self, epoch):` 데이터를 훈련을 시키고  
`def test(self):` 훈련된 데이터에 대해서 성능을 측정하고  
`def learning(self):`  실제로 러닝을 해본다.  

<br>




