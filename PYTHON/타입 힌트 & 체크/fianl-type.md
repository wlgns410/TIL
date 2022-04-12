# final 타입

final은 아무도 건들지 못하게 타입을 고정시키는 것이다.  
하지만, Python 은 동적 언어이기 때문에 별도로 타입을 지정하지도 않으며, final 이라는 키워드도 없다고 한다.  
Python 3.8 부터는 typing.Final 를 사용해서, 변수의 재할당을 방지할 수 있다고 한다.  

<br>

[참고](https://velog.io/@pm1100tm/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%83%81%EC%88%98%EB%A5%BC-%EC%A0%95%EC%9D%98%ED%95%98%EA%B3%A0-%EC%82%AC%EC%9A%A9%ED%95%A0%EA%B9%8C)

<br>

# 예시
이미 할당해서 다시 상수를 할당할 수 없음

```
from typing_extensions import Final

RATE: Final = 300

RATE = 300
```

```
type.py:148: error: Cannot assign to final name "RATE"
Found 1 error in 1 file (checked 1 source file)
```