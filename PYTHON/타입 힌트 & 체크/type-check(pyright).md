# 타입 체크 2

<br>

`type-hint.md` 다음 블로깅입니다. 

<br>

mypy보다 빠르고 안정적인 라이브러리가 있다.  
명령어 차이만 있고 똑같기 때문에 아무거나 써도 상관은 없다.  
pip으로도 설치가능하게 바뀌었다고 하는데, 나는 에러가 떠서 그냥 노드를 설치해서 했다.

```
pyright.errors.VersionCheckFailed: Could not find version from `npx --version`, see output above
```

<br>

우선 노드를 설치하고,
<br>

> sudo npm install -g pyright

<br>

> pyright --help

<br>

설치가 다 된것을 확인하고 스크립트를 실행한다.

<br>

> pyright type.py

```
def type_check(obj: Any, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError(f"type error : {typer}")

def cal_add(x: int, y:int) -> int:

    type_check(x, int)
    type_check(y, int)
    return x + y

print(cal_add(1, 3))

```

<br>
성공시

<br>

```
No configuration file found.
No pyproject.toml file found.
stubPath /Users/jihoon/project/python-class/typings is not a valid directory.
Assuming Python platform Darwin
Searching for source files
Found 1 source file
0 errors, 0 warnings, 0 informations
Completed in 1.011sec
```

<br>

실패시

<br>

```
No configuration file found.
No pyproject.toml file found.
stubPath /Users/jihoon/project/python-class/typings is not a valid directory.
Assuming Python platform Darwin
Searching for source files
Found 1 source file
/Users/jihoon/project/python-class/type.py
  /Users/jihoon/project/python-class/type.py:40:18 - error: Argument of type "Literal['3']" cannot be assigned to parameter "y" of type "int" in function "cal_add"
    "Literal['3']" is incompatible with "int" (reportGeneralTypeIssues)
1 error, 0 warnings, 0 informations
Completed in 0.792sec
```

<br>

`pyright` 라이브러리도 타입 체킹만 해주고 결과값을 알려주지는 않는다는 단점이 있다.  

<br>

> pyright type.py && python type.py 

<br>

```
No configuration file found.
No pyproject.toml file found.
stubPath /Users/jihoon/project/python-class/typings is not a valid directory.
Assuming Python platform Darwin
Searching for source files
Found 1 source file
0 errors, 0 warnings, 0 informations
Completed in 0.853sec
4
```

<br>

하지만, mypy, pyright는 python에서 공식적으로 지원하는 라이브러리가 아니다보니 라이브러리를 쓰기보다는 타입을 체크하는 함수를 만들고  
유닛 테스트를 하는 것을 추천한다고 한다.

<br>