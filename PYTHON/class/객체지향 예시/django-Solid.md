# django model Solid 끄적끄적

맞는지는 모름. 그냥 클린코드 공부중  

<br>

## 단일 책임 원칙(single responsibility principle)

```
from django.db import models


class Snack(models.Model):
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    count = models.IntegerField()
    degress = models.IntegerField(blank=False)
    sugar = models.IntegerField(blank=False)
    sale = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
```

위 같은 코드가 있다고 치자.  

단일 책임 원칙은 하나의 클래스는 하나의 책임을 져야한다는 원칙이다.  
모델을 분리시켜주자.  

<br>

```
from django.db import models

class IceCremam(models.Model):
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    count = models.IntegerField()
    degress = models.IntegerField(blank=False)
    sale = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'


class Snack(models.Model):
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    count = models.IntegerField()
    sugar = models.IntegerField(blank=False)
    sale = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

```

<br>

## 개방/폐쇄의 원칙 (Open-Closed Principle)

확장에 대해 열려 있어야 하고, 수정에 대해서는 닫혀 있어야 한다 라고 한다.  
더 리팩토링하자.

<br>

sale 필드를 필터를 위한 QuerySet 중복 코드를 해결하기 위해 위에서 학습한 get_queryset을 재정의 하는  
custom Manager를 작성하고 sale_objects 이름으로 정의한다.  

앞으로 생기는 코드들도 SaleManager 클래스를 상속함으로서 수월하게 확장할 수 있다.  

<br>

```
class SaleManager(models.Manager):
    
    def get_queryset(self):
        return super().get_queryset().filter(sale=True)


class IceCremam(AbstractBase):
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    count = models.IntegerField()
    degress = models.IntegerField(blank=False)
    objects = models.Manager()
    sale_objects = SaleManager()


class Snack(AbstractBase):
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    count = models.IntegerField()
    sugar = models.IntegerField(blank=False)
    objects = models.Manager()
    sale_objects = SaleManager()
```

<br>

## 리스코프 치환 원칙(Liskov Substitution Principle)

어떤 하위 타입을 사용해도 실행에 따른 결과는 같아야 한다는 원칙이다.  
type hint를 기재하자.  
get_queryset(self) -> bool로 return의 type hint를 알려주자.  

<br>


```
class SaleManager(models.Manager):
    
    def get_queryset(self) -> bool:
        return super().get_queryset().filter(sale=True)


class IceCremam(AbstractBase):
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    count = models.IntegerField()
    degress = models.IntegerField(blank=False)
    objects = models.Manager()
    sale_objects = SaleManager()


class Snack(AbstractBase):
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    count = models.IntegerField()
    sugar = models.IntegerField(blank=False)
    objects = models.Manager()
    sale_objects = SaleManager()
```

<br>

## 인터페이스 분리 원칙(Interface Segregation Principle)

여러개의 메서드를 가진 인터페이스가 있다면 매우 정확하고 구체적인 구분에 따라  
더 적은 수의 메서드를 가진 여러개의 메서드로 분할하는 것이 좋다는 원칙이다.

더 작은 수의 클래스로 쪼개보자  
중복된 코드들을 상속을 활용하여 제거하기로 하자.  
여러개의 클래스로 나눠보자.

<br>

```
class SaleManager(models.Manager):
    
    def get_queryset(self) -> bool:
        return super().get_queryset().filter(sale=True)

class AbstractBase(models.Model):
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    count = models.IntegerField()
    objects = models.Manager()

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.name}'


class IceCremam(AbstractBase):
    degress = models.IntegerField()


class Snack(AbstractBase):
    sugar = models.IntegerField()
```

<br>

## 의존성 역전 원칙(Dependency Inversion Principle)

<br>

고수준 모듈은 저수준 모듈의 구현에 의존해서는 안 된다.  
저수준 모듈이 고수준 모듈에서 정의한 추상 타입에 의존해야 한다.  

즉, 자식 모델에서 새로운 매니저가 추가되면 Default manager가 선정하는 우선순위에 의해 변경되는 이슈를 막아보자.

<br>

위 문제를 막기위해 django model manager에서 제공하는 `default_manager_name`을 사용  

<br>

```
class SaleManager(models.Manager):
    
    def get_queryset(self) -> bool:
        return super().get_queryset().filter(sale=True)

class AbstractBase(models.Model):
    price = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    count = models.IntegerField()
    objects = models.Manager()

    class Meta:
        abstract = True
        default_manager_name = 'objects'

    def __str__(self):
        return f'{self.name}'


class IceCremam(AbstractBase):
    degress = models.IntegerField()


class Snack(AbstractBase):
    sugar = models.IntegerField()


class NoSaleManager(models.Manager):
    def get_queryset(self) -> bool:
        return super().get_queryset().filter(sale=False)

class Reply(AbstractBase):
    no_active_objects = NoSaleManager()
```

<br>

하지만, 하부 모델인 reply에서도 default_manager_name을 지정해버리면  
의존성 역전 원칙이 깨지는 문제가 발생한다고 한다.  
이 문제의 해결방법은 팀끼리의 컨벤션을 위한 문서화가 필수라고 한다.

<br>

