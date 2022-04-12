# callabel 객체
전달받은 object 인자가 호출 가능한지 여부를 판단한다. 

<br>

argument : 호출 가능 여부를 판단할 object 인자 하나를 넘겨준다.  
return value : 인자로 전달받은 object가 호출 가능한 object일 경우 True, 아닐 경우 False를 반환한다.  

<br>

```
def add(a:int, b:int) -> int:
    return a + b

print(add(1,3))
```

```
Success: no issues found in 1 source file
4
```

<br>

하지만, 함수내에서 return이 없어진다면?

```
def add(a:int, b:int) -> int:
    print(a + b)

print(add(1,3))
```

```
type.py:44: error: Missing return statement
Found 1 error in 1 file (checked 1 source file)
```

<br>

따라서 callable 객체도 지워준다.

```
def add(a:int, b:int):
    print(a+b)

print(add(1,3))
```

```
4
None
```

<br>

# 함수를 넘겨줄때는 어떻게 하는지? -> callable 함수를 사용

<br>

```
from typing import Callable

def add(a:int, b:int) -> int:
    return a + b


def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)

print(foo(add))
```

```
Success: no issues found in 1 source file
5
```

<br>

호출할 수 없는 함수를 호출했을 때

```
def add(a:int, b:int) -> int:
    return a + b

def test():
    pass

def foo(func: Callable[[int, int], int]) -> int:
    return func(2, 3)

print(foo(test))
```

```
type.py:59: error: Argument 1 to "foo" has incompatible type "Callable[[], Any]"; expected "Callable[[int, int], int]"
Found 1 error in 1 file (checked 1 source file)
```

<br>

# 예시

```
from typing import List, Callable

def print_func_result(func: Callable[[List[int], int], int], arg1: List[int], arg2: int):
    return func(arg1, arg2)

def list_sum(ll: List[int], to: int):
    x = ll[:to]
    return sum(x)

result = print_func_result(list_sum, [1,2,3], 2)
print(result)
```

```
Success: no issues found in 1 source file
3
```