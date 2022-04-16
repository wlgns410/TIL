# 네이버 뉴스 api 웹스크래핑

공식문서 참조

```
curl "https://openapi.naver.com/v1/search/news.xml?query=%EC%A3%BC%EC%8B%9D&display=10&start=1&sort=sim" \
    -H "X-Naver-Client-Id: {애플리케이션 등록 시 발급받은 client id 값}" \
    -H "X-Naver-Client-Secret: {애플리케이션 등록 시 발급받은 client secret 값}" -v
```

<br>

포스트맨을 이용한다.
공식문서를 보고 키값을 그대로 입력한다.

<br>

<img width="1035" alt="스크린샷 2022-04-16 오후 3 00 36" src="https://user-images.githubusercontent.com/81137234/163663797-0821d7c3-baca-445d-8cfd-16846fbc2326.png">

<br>


# 카카오 검색


공식문서 참조

```
curl -v -X GET "https://dapi.kakao.com/v2/search/web" \
--data-urlencode "query=이효리" \
-H "Authorization: KakaoAK ${REST_API_KEY}"
```

<br>

![스크린샷 2022-04-16 오후 3 09 10](https://user-images.githubusercontent.com/81137234/163663976-280c8b2b-2ecd-4bfa-800a-616e37afe456.png)

<br>

추가적인 파라미터도 입력 가능하다.

<br>

<img width="871" alt="스크린샷 2022-04-16 오후 3 12 49" src="https://user-images.githubusercontent.com/81137234/163664088-d63a822a-6a6c-4dca-9a66-17f3c5ad62da.png">

<br>

![스크린샷 2022-04-16 오후 3 12 58](https://user-images.githubusercontent.com/81137234/163664101-41be60b0-0f14-4aae-acd8-ff7250166998.png)

<br>

이걸 코드로 바꿔보자.

<br>

```

import aiohttp
import asyncio

async def fetcher(session, url):

    headers = {
        "Authorization" : "KakaoAK " + "시크릿키"
    }

    async with session.get(url, headers=headers) as response:
        result = await response.json()
        print(result)


async def main():
    base_url = "https://dapi.kakao.com//v2/search/image"

    keyword = "python"

    urls = [f"{base_url}?query={keyword}&page={i}&size=5" for i in range(1, 21)]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetcher(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())

```

```
...

'documents': [{'collection': 'blog', 'datetime': '2020-08-17T18:55:00.000+09:00', 'display_sitename': '네이버블로그', 'doc_url': 'http://blog.naver.com/kyj0423282/222063113448', 'height': 543, 'image_url': 'http://postfiles3.naver.net/MjAyMDA4MTdfMTcw/MDAxNTk3NjU4MDQyODk1.PCR2hvTOD8CsV9_5Xlrs0A-DVthn4gkrC6FF-ixGfBUg.LyfCpeg3P3OmLeIpC0GXUrl0Iqv-xhdAJXjfvRnkkkwg.JPEG.kyj0423282/%ED%8C%8C%EC%9D%B4%EC%8D%AC_%EC%84%A4%EC%B9%98_PYTHON_%EA%B8%B0%EC%B4%88_%EA%B0%95%EC%A2%8C_%EC%9D%B8%EA%B0%95_%EA%B5%90%EC%9C%A1_23.jpg?type=w966', 'thumbnail_url': 'https://search3.kakaocdn.net/argon/130x130_85_c/CWsK2gg8TNx', 'width': 966}, {'collection': 'blog', 'datetime': '2022-03-18T01:20:05.000+09:00', 'display_sitename': '티스토리', 'doc_url': 'http://darkgraycat.tistory.com/108', 'height': 526, 'image_url': 'https://k.kakaocdn.net/dn/wWnro/btrwhTJc7O4/Dj329EDhQl2wkjEWDkEIV1/img.png', 'thumbnail_url': 'https://search2.kakaocdn.net/argon/130x130_85_c/G55UnxjygON', 'width': 619}, {'collection': 'blog', 'datetime': '2022-03-28T19:22:39.000+09:00', 'display_sitename': '티스토리', 'doc_url': 'http://jayden1116.tistory.com/457', 'height': 469, 'image_url': 'https://user-images.githubusercontent.com/86241737/160370423-03db4aa9-bdf9-40bb-8dc0-65f4fa097bb0.png', 'thumbnail_url': 'https://search4.kakaocdn.net/argon/130x130_85_c/ExdyW4aEpBU', 'width': 755}, {'collection': 'blog', 'datetime': '2021-12-22T15:36:17.000+09:00', 'display_sitename': '티스토리', 'doc_url': 'http://cometitstudy.tistory.com/34', 'height': 243, 'image_url': 'https://k.kakaocdn.net/dn/baMoJY/btrozx8KF7M/NRb1T9QgzRX1aS0gRRQYc1/img.png', 'thumbnail_url': 'https://search3.kakaocdn.net/argon/130x130_85_c/Ic8y1X9mWkS', 'width': 218}, {'collection': 'blog', 'datetime': '2022-04-01T23:04:39.000+09:00', 'display_sitename': '티스토리', 'doc_url': 'http://gotopark.tistory.com/55', 'height': 175, 'image_url': 'https://k.kakaocdn.net/dn/b03yzw/btrybMCSy9C/XiNgToMghfSHK44oqIU10K/img.png', 'thumbnail_url': 'https://search2.kakaocdn.net/argon/130x130_85_c/40RhMuux71t', 'width': 296}], 'meta': {'is_end': False, 'pageable_count': 3956, 'total_count': 1147480}}

...

```


```
import aiohttp
import asyncio


async def fetcher(session, url):

    headers = {
        "X-Naver-Client-Id" : "",
        "X-Naver-Client-Secret" : ''
    }

    async with session.get(url, headers=headers) as response:
        result = await response.json()
        print(result)
        items = result['items']
        images = [item['link'] for item in items]
        print(images)


async def main():
    base_url = "https://openapi.naver.com/v1/search/image"

    keyword = "python"

    urls = [f"{base_url}?query={keyword}&start={1 + i *20}&display=20" for i in range(10)]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetcher(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())
```

<br>

# 시크릿키 관리

secrets.json 파일을 판 뒤  
gitignore에 입력  
참고로 json 파일은 ""로 감싸야함

```
# secrets.json

{
    "X-Naver-Client-Id" : "",
    "X-Naver-Client-Secret" : ""
}
```

<br>

그 뒤, config.py를 작성  
`json_path`가 path 라이브러리를 통해서 경로를 가져온다(해당 폴더)  
`parent`는 해당 파일의 바로 상위 경로를 말한다. (1번 붙이면 바로위, 2번 붙이면 위의 위 폴더 경로)  
그래서 상위 폴더(Base_url)의 하부 폴더인 secret.json을 열어서(`with open`) 읽는다.  
거기서 `secrets[key]`은 파일의 키 밸류 값을 뽑아서 리턴한다는 뜻이다.  


<br>

```
import json
from pathlib import Path
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent


def get_secret(
    key: str,
    default_value: Optional[str] = None,
    json_path: str = str(BASE_DIR / "secrets.json"),
):

    with open(json_path) as f:
        secrets = json.loads(f.read())
    try:
        return secrets[key]
    except KeyError:
        if default_value:
            return default_value
        raise EnvironmentError(f"Set the {key} environment variable.")
```

<br>

아래와 같이 시크릿키를 불러와보자.

```
import aiohttp
import asyncio
from config import get_secret

async def fetcher(session, url):

    headers = {
        "X-Naver-Client-Id" : get_secret('X-Naver-Client-Id'),
        "X-Naver-Client-Secret" : get_secret('X-Naver-Client-Secret')
    }

    async with session.get(url, headers=headers) as response:
        result = await response.json()
        print(result)
        items = result['items']
        images = [item['link'] for item in items]
        print(images)


async def main():
    base_url = "https://openapi.naver.com/v1/search/image"

    keyword = "python"

    urls = [f"{base_url}?query={keyword}&start={1 + i *20}&display=20" for i in range(10)]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetcher(session, url) for url in urls])


if __name__ == "__main__":
    asyncio.run(main())
```

```
...

['https://i.stack.imgur.com/q4Uct.png', 'https://i.pinimg.com/736x/22/92/9d/22929d2ed45e59a262997e522d38b470.jpg', 'https://i.stack.imgur.com/dXDIL.jpg', 'https://i.stack.imgur.com/jE70M.jpg', 'https://i.stack.imgur.com/Yy6wb.png', 'https://i.stack.imgur.com/odXAb.png', 'https://www.chess.com/share/user/python_nerd7', 'https://i.stack.imgur.com/DPm6m.png', 'https://i.stack.imgur.com/o84sK.png', 'https://live.staticflickr.com/3203/3066051352_2c3685cab2_b.jpg', 'https://i.pinimg.com/originals/2c/a5/52/2ca552c450326d79242b81de996e3e19.jpg', 'https://media-exp1.licdn.com/dms/image/C4E12AQHNG8EvDyjBZQ/article-cover_image-shrink_600_2000/0/1533802387515?e=1654732800&v=beta&t=iFm883nx4WBe0CNmZ5qqparLy72p54ecjcqUaXqY_H0', 'https://lh5.ggpht.com/udYPmfUN-arbLGBhfT_f67HW17DvVid34fnpIlpaNM6OTlJ3OJbOng0RuVWTrIoYUU0c9x2-31z1Oxx4-uQz=s600', 'https://h7.alamy.com/comp/B34X6T/burmese-rock-python-python-molurus-bivittatus-B34X6T.jpg', 'https://i.stack.imgur.com/Jh0TO.png', 'https://inaturalist-open-data.s3.amazonaws.com/photos/151626902/large.jpg', 'https://live.staticflickr.com/2896/14135090372_51cd378d08_b.jpg', 'https://i.stack.imgur.com/ojppY.png', 'https://seeklogo.com/images/P/python-logo-C50EED1930-seeklogo.com.png', 'https://i.stack.imgur.com/ptOjJ.png']
```

<br>

시크릿키 관리를 잘하자.

<br>
