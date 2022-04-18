# fastapi로 프로젝트를 만들어보자

우선 asgi와 uvicorn을 알아보자.

- asgi : 애플리케이션 프로그램의 실행 결과를 웹 서버에 전달, 웹 서버는 asgi로부터 전달받은 응답 결과를 웹 클라이언트에 전달

웹서버 게이트웨이  
추가적으로 asgi는 비동기적인 구현도 지원함  

- Uvicorn : asgi 웹 어플리케이션을 실행하는 서버


`Uvicorn - asgi - fastapi - python` 의 구조.

<br>

# fastapi 간단실행

<br>

> 

> pip install fastapi

> pip install uvicorn

<br>

매우 간단하다.  
아래 구조로 이루어져 있다.
fastapi 인스턴스를 생성해서 url을 호출 -> django urls를 바로 사용  

<br>

특이점은 fastapi는 type hint가 강제된다. -> django와 차이점  

<br>




```
fastapi 
   -> app
      -> main.py
```

```
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
```

<br>


런서버를 한다.

> uvicorn app.main:app --reload

또는 app 폴더 안으로 들어간 뒤,

> uvicorn main:app --reload

하면 runserver가 정상적으로 된다.

<br>

공식문서가 매우 친절하다.  

```
main: main.py 파일 (파이썬 "모듈")  
app: the object created inside of main.py with the line app = FastAPI()  
--reload: 코드가 변경된 후 서버 재시작하기. 개발환경에서만 사용  
```

<br>

# 파이썬 스크립트로 runserver 실행하기

server.py에 코드를 작성한다.  
`__name__` 은 interpreter가 실행 전에 만들어 둔 글로벌 변수이다.  
하지만 파이썬에서는 main이라는 파일이 존재하지 않는다 -> c, java에서의 동작방식임  
대신 파이썬은 들여쓰기가 존재한다.  
파이썬은 main문이 없는 대신에, 들여쓰기가 되지 않은 Level0의 코드를 가장 먼저 실행한다고 한다.  


<br>

```
`__name__`는 현재 모듈의 이름을 담고있는 내장 변수이다. 이 변수는 직접 실행된 모듈의 경우 __main__이라는 값을 가지게 되며, 직접 실행되지 않은 import된 모듈은 모듈의 이름(파일명)을 가지게 된다고 한다.
```

<br>

```
결론을 짓자면 모듈에 if __name__=="__main__"이라는 조건문을 넣어주고 그 아래는 직접 실행시켰을 때만 실행되길 원하는 코드들을 넣어주는 것
```

<br>

```
import uvicorn


if __name__ == "__main__":
    uvicorn.run('app.main:app', host="localhost", port=8000, reload=True)
```

<br>

```
❯ python server.py
INFO:     Will watch for changes in these directories: ['/Users/jihoon/project/python/fastapi']
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [19095] using statreload
INFO:     Started server process [19097]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

제대로 동작한다.

<br>

# fastapi docs

아래 사이트에 접속하면 django swagger와 같은 UI를 보여준다. -> 설치없이 api docs를 제공해줌

>  http://127.0.0.1:8000/docs 

<br>

# jinja 템플릿 엔진 사용하기

<br>

> pip install jinja2

> pip install aiofiles

<br>

구조

```
fastapi 
   -> app
      -> templates
        -> item.html
      -> main.py
   server.py
   requirements.py

```

<br>

```
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})
```

<br>

`app = FastAPI()` : FastAPI 인스턴스로 객체를 뽑아냄(싱글톤 패턴)  
`app.mount("/static", StaticFiles(directory="static"), name="static")` : StaticFiles는 js, css, img를 관리하는 폴더 -> django에서도 이와 같이 관리함  

`templates = Jinja2Templates(directory="templates")` : html 파일 보관 -> django 와 같음  

<br>

` templates.TemplateResponse("item.html", {"request": request, "id": id})`이므로 파일 이름을 item.html로 해줌

```
<html>
<head>
    <title>Item Details</title>
</head>
<body>
    <h1>Item ID: {{ id }}</h1>
</body>
</html>
```

<br>

런서버를 하는 방법이 2가지가 있다고 했다.  

```

templates = Jinja2Templates(directory="app/templates") 일때는 
uvicorn app.main:app --reload 로 런서버


templates = Jinja2Templates(directory="templates") 일때는  
app 폴더 안으로 들어간 뒤, uvicorn main:app --reload 로 런서버

```

아까도 적었듯, 코드에 따라서 runserver 명령어가 달라진다.  
절대경로로 지정해서 코드를 고정시키자.

```
런서버를 한다.

from pathlib import Path
from fastapi.templating import Jinja2Templates


BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=BASE_DIR / "templates")
```

이럼 이제 app 안에 들어가서 런서버를 하는게 아니라 `uvicorn app.main:app --reload`로 강제된다. -> django에서는 manage.py가 위치한 곳에서만 runserver가 되도록 강제함  

<br>

# request 

`@app.get`이 어떻게 `request: Request, id: str`을 인식할까?  
바로 타입힌트를 통해서 인식하게 된다.  
request를 더 알아보자.

```
async def read_item(request: Request, id: str):
    print(request)
```
```
<starlette.requests.Request object at 0x7ff330fc1730>
```

request 객체가 나온다.

<br>

request의 dir(객체의 메소드)를 알아보자  

header값 정보도 알아보자.

```
# request의 dir
['__abstractmethods__', '__class__', '__contains__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', '_abc_impl', '_cookies', '_headers', '_is_disconnected', '_query_params', '_receive', '_send', '_stream_consumed', 'app', 'auth', 'base_url', 'body', 'client', 'close', 'cookies', 'form', 'get', 'headers', 'is_disconnected', 'items', 'json', 'keys', 'method', 'path_params', 'query_params', 'receive', 'scope', 'send_push_promise', 'session', 'state', 'stream', 'url', 'url_for', 'user', 'values']

# header
[(b'host', b'127.0.0.1:8000'), (b'connection', b'keep-alive'), (b'cache-control', b'max-age=0'), (b'sec-ch-ua', b'" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"'), (b'sec-ch-ua-mobile', b'?0'), (b'sec-ch-ua-platform', b'"macOS"'), 
...
```

<br>

# 검색 만들기

```
<center>
        <form id="search_form" action="/search">
            <input type="search" placeholder="keyword" id="search_input" name="q">
            <button type="submit">검색</button>
        </form>
        
</center>


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    print(q)

    return templates.TemplateResponse("./index.html", {"request": request})
```

```
# terminal

ddd
```

<br>

검색어를 입력하면 fastapi가 파싱을 해서 터미널에 출력을 해준다.  
`q: str` 인자에 있는 q에 자동으로 넣어주는 것이다.  
이것은 html 파일에 있는 `name="q"`를 통해 html과 view가 연결되는 django와 구동방식이 같다.  
만약 q:str 대신 e:str로 바꾸다면 template과 view의 연결이 끊겨서 에러가 뜰 것이다.  

<br>

그리고 view의 값을 template을 통해 출력하고 싶다면, view에서의 key 값을 template에 넣어주면 된다.

```
<main>
    {{ keyword }}
</main>


@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):
    print(q)

    return templates.TemplateResponse("./index.html", {"request": request, "keyword":q})
```

```
WARNING:  StatReload detected file change in 'app/main.py'. Reloading...
INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [9643]
INFO:     Started server process [11874]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:54938 - "GET /search HTTP/1.1" 422 Unprocessable Entity
이지훈
```

<br>

제대로 출력된다.  

<br>

요약하자면, keyword에 검색을 누르면  
`action="/search"`을 통해서 `name="q"`에 검색어가 들어간다.  
해당하는 검색어가 붙은 url로 요청을 한다.  
요청이 해당하는 라우터와 매칭을 한다.`app.get("/search")`  
해당 라우터에서 `q: str` 처럼 타입힌팅을 통해 인자를 인식한다.  
이 인자를 `return templates.TemplateResponse("./index.html", {"request": request, "keyword":q})`처럼 컨텍스트에 넣어서 response로 보내준다.  
그럼 컨텍스트에서 `키`값을 받아서 template에서 렌더링하게 되는 것이다.  

