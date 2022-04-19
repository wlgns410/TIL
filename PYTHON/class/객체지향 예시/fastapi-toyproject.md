# 토이프로젝트

<br>

우선 코드를 조금 바꿨다.  
sqlalchemy 를 이용해서 mysql과 연결할 것이다.

<br>

구조

```
app
    models
        __init__.py
        books.py
    templates
        index.html
    book_scraper.py
    config.py
    main.py
secret.json
server.py
```

<br>

sqlalchemy로 Mysql과 연결시킨다.

```
from sqlalchemy import create_engine, MetaData
from app.config import MYSQL_URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#  디비 세팅
db_engine = create_engine(MYSQL_URL)
db_metadata = MetaData()
conn = db_engine.connect()


print("디비 연결 됨")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()
```

연결한 객체를 books.py에 가져와서 테이블을 구성한다.
그리고 data type을 지정해 validation하기 위한 모델을 만든다.

```
from pydantic import BaseModel
from sqlalchemy import Column, Table
from sqlalchemy.sql.sqltypes import INTEGER, String
from app.models import db_metadata, db_engine

class Book(BaseModel):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"



books = Table('books', db_metadata,
              Column('id', INTEGER(), primary_key=True),
              Column('keyword', String(255)),
              Column('publisher', String(255)),
              Column('price', INTEGER()),
              Column('image', String(255)),
              )

db_metadata.create_all(db_engine)
# db : fastapi -> collection : books -> document (keyword, publisher ....)
```

<br>

main.py에서 crud를 작성한다.

<br>

```
@app.get('/', response_class=HTMLResponse)
def fetch_all(request: Request):
    conn.execute(books.select()).fetchall()
    return templates.TemplateResponse("./index.html", {"request": request, "title": "책소개"})

@app.post('/', response_class=HTMLResponse)
def create_user(book: Book, request: Request, q: str):
    conn.execute(books.insert().values(keyword="파이썬", publisher="Bjpublic", price=1200, image='me.png'))
    conn.execute(books.select()).fetchall()
    return templates.TemplateResponse("./index.html", {"request": request, "keyword":q})
```

sql 문법을 이용해서 insert 및 select()해서 데이터를 넣거나 가져오는 작업이다. 대충 이렇게 이루어져있다.

<br>

# 프로젝트 소개

네이버 openapi로 book 정보를 가져오는 스크래퍼 만들기  
위 코드를 활용해서 스크래퍼를 만들어보자.

<br>

```
import aiohttp
import asyncio

from app.config import get_secret


class NaverBookScpaer:

    NAVER_API_BOOK = "https://openapi.naver.com/v1/search/book"
    NAVER_API_ID = get_secret("NAVER_API_ID")
    NAVER_API_SECRET = get_secret("NAVER_API_SECRET")


    # 데이터를 요청하는 함수
    @staticmethod
    async def fetch(session, url, headers):
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                result = await response.json()
                return result

    
    def unit_url(self, keyword, start):
        return {
            "url": f"{self.NAVER_API_BOOK}?query={keyword}&display=10&start={start}",
            "headers": {
                "X-Naver-Client-Id": self.NAVER_API_ID,
                "X-Naver-Client-Secret": self.NAVER_API_SECRET
            }
        }

    # fetch -> api url 데이터를 요청 
    # 요청하는 페이지들을 동시성을 적용해서 빠르게 스크래핑을 함
    async def search(self, keyword, total_page):
        #  1이 들어오면 1 + 10까지, 4가 들어오면 4부터 14까지
        apis = [self.unit_url(keyword, 1 + i * 10) for i in range(total_page)]

        async with aiohttp.ClientSession() as session:
            all_data = await asyncio.gather(
                *[NaverBookScpaer.fetch(session, api["url"], api["headers"]) for api in apis]
            )

            return all_data

    # async 함수를 실행하려면 run을 해야하가 때문에 적어줌
    def run(self, keyword, total_page):
        return asyncio.run(self.search(keyword, total_page))

    
if __name__ == "__main__":
    scraper = NaverBookScpaer()
    print(scraper.run("파이썬", 2)) # 이 결과값이 run 메서드고, run 메서드 결과값이 search의 result
    print(len(scraper.run("파이썬", 5)))


```

statcmethod를 사용한 이유는 정적 함수로서 의미를 가질 수 있기에 사용  
인스턴스 매소드, 클래스 매소드로도 사용되지 않기 때문이다.  
만약 해당 인스턴스에 집중하고 싶다면 인스턴스 메소드로 설계해야한다.  

<br>

우선 클래스 변수를 지정해서 클래스 내에서 사용하는 변수를 만든다.  
데이터를 요청하는 메서드를 만든다. 여기서는 session, url, header가 필요하다.  

<br>
fetch 험수로 네이버에 접속해 session을 유지시킨다.  
unit_url 메서드를 통해 naver에 id, secret 키를 던져준다.  

그럼 search 함수로 키워드, page를 얼마나 받을것인지 값을 던져준다.
async 함수를 사용했으니 run을 해준다.  

<br>

이 파일을 실행시키기 위해 __name__=="__main__"을 작성한다.  

<br>

아래의 사항에 따라 코드를 작성한다.

```
1. 요구사항
# 데이터 수집기로 해당 검색어 데이터 수집
# DB에 수집된 데이터를 저장
# 수집된 각각의 데이터에 대해 DB에 들어갈 모델 인스턴스를 찍는다.
# 각 모델 인스턴스를 DB에 저장

2. 예외처리
# 검색어가 없다면 사용자에게 검색을 요구 return
# 해당 검색어에 대해 수집된 데이터가 이미 DB에 존재한다면 해당 데이터를 사용자에게 보여줌 return
```

```
@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str):

    keyword = q

    # 검색어가 없다면 사용자에게 검색을 요구 return
    if not keyword:
        context = {"request":request, "title":"책 다방"}
        return templates.TemplateResponse("./index.html", context)

    naver_book_scraper = NaverBookScpaer()
    book_obj = await naver_book_scraper.search(keyword, 1)

    for book in book_obj:

        book_obj2=book['items']

        for i in book_obj2:

            conn.execute(books.insert().values(keyword=keyword, publisher=i["publisher"], price=i["price"], image=i['image']))
            conn.execute(books.select()).fetchall()
        
            
    return templates.TemplateResponse("./index.html", {"request": request, "title": "책 검색기", "books":book_obj2})
```

<br>

naver_book_scraper를 인스턴스로 생성해서 키워드와 page 1개를 가져오게 했다.  

근데, response를 받아보니, 2중 for문으로 파싱을 해야했다. 그래서 2중 for문을 돌렸다.  
sqlalchemy로 post하기 위해서 insert()하고 values를 넣어줬다.  
이 값을 book_obj2에 담고 랜더링 해줬다.  

```
<main>
        <!-- books는 search함수의 키값  -->
      {% if books %}
      <!--  -->
      <center>
        <h3 style="color: gray">{{books|length}}개 데이터 수집..</h3>
      </center>
      <section>
          <!-- books 순회함 -->
        {% for book in books %}
        <div>
          <img src="{{book.image}}" width="150px" height="200px" />
          <p>
            {% if book.publisher|length > 10 %}
            <!--  -->
            {{book.publisher[:10]}}...
            <!--  -->
            {% else %} {{book.publisher}} {% endif %}
          </p>
          <p>{{book.price}} 원</p>
        </div>
        {% endfor %}
      </section>

      <hr />
      {{books}}
      <!--  -->
      {% else %}
      <center><h3 style="color: gray">키워드를 입력하세요</h3></center>
      {% endif %}
    </main>
```

view에 매칭되게 template에 키를 넣어줬다.  

<br>

![스크린샷 2022-04-19 오후 3 27 59](https://user-images.githubusercontent.com/81137234/163939775-8b6a006d-32bc-4d77-9952-40a539184969.png)

<br>

앞으로 추가할 것

update, delete  
해당 검색어에 대해 수집된 데이터가 이미 DB에 존재한다면 해당 데이터를 사용자에게 보여줌 return
로그인, 회원가입  
필터링

<br>