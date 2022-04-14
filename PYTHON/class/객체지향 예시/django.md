# django에서의 객체지향 예시
django에서 객체지향은 어떻게 사용되고 있는지 알아보자.

<br>

다음은 모델을 작성하는 방법이다.

<br>

```
class Student(models.Model):

    """
    student model
    """
    product_name = models.CharField(max_length=100)
    product_thumbnail = models.URLField()
    product_price = models.PositiveIntegerField() # 상품가격 : 양수만 가지도록
    regular_price = models.PositiveIntegerField() # 정가 :  양수만 가지도록
    is_soldout = models.BooleanField(null=True)
    tag = models.JSONField()
```

<br>

student 클레스를 작성한다.  
`models.Model` 장고에서 지원해주는 모델을 상속받는다.  
`"""`을 통해 알려야할 것을 기재한다.  
`product_name(클래스변수)` 작성을 통해 클래스 내에서 사용할 변수를 작성한다.  
객체지향을 이용해서 코드를 짠다는 것은 이미 갖추어진 것을 사용만 하면 된다는 것이다.  
이 이유가 객체지향을 사용하는 이유이다.  

<br>

오버라이딩(덮어씌우기) 예시

<br>

```
class MakeProduct(CreateAPIView):
    queryset = Merchandise.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(merchandise=request.data)
        return Response({"message":"SUCCESS"}, status = status.HTTP_201_CREATED)
```

<br>

django rest framework 공식문서를 가보면 `CreateAPIView`가 가지고 있는 여러 메소드들이 있다.  
예를들어 `def post(self, request):` 처럼 POST 를 하고 싶다고 가정하자.  
메소드들을 일일히 작성하는 것이 아니라, 프레임워크에서 제공하는 메소드들을 가지고 기능을 조금씩만 바꾸는 것만으로 코드를 작성할 수 있다는 것이다.  
생산성 향상을 위해 프레임워크를 쓰는 이유가 이 때문이다.  

<br>