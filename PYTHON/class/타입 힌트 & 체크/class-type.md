# 클래스 체크

파이썬은 함수, 클래스 등 모든 것을 받을 수 있다.  
이전에는 함수를 받았으니 이번에는 클래스를 받아보자. -> callable-type.md 참고

<br>

```
class Hello:
    def world(self) -> int:
        return 7


hello: Hello = Hello()

def foo(instance: Hello) -> int:
    return instance.world()

print(foo(hello))
```

```
Success: no issues found in 1 source file
7
```

<br>

다른 클래스를 받았을 때(에러 발생 경우)

```
class Hello:
    def world(self) -> int:
        return 7

class say:
    pass

hello: Hello = Hello()

def foo(instance: Hello) -> int:
    return instance.world()

print(foo(say))
```

```
type.py:87: error: Argument 1 to "foo" has incompatible type "Type[say]"; expected "Hello"
Found 1 error in 1 file (checked 1 source file)
```