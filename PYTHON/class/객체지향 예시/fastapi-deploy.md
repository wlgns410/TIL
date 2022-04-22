# 간단히 만든걸 배포해보자

- lightsail을 이용했다.

ec2와 달리 lightsail은 더 간편했다. aws permission key를 가지고 로그인하는게 아니라  
자동으로 instance 서버에 로그인하게 만들어줬다.  

<br>

배포용 코드를 살짝 바꾼다.  

<br>

```
# server.py 코드

import uvicorn

if __name__ == "__main__":
    uvicorn.run('app.main:app', host="0.0.0.0", port=80, reload=False)
```

localhost로 되어있어서 우선은 다 들어오게 0.0.0.0으로 바꿨고, 포트도 8000->80으로 바꿨다.  
그리고 reload 속성도 True -> False로 바꿨다.

<br>

local용이랑 server용으로 나눠서 관리하면 편할것이다.  

<br>

그리고 secret.py 코드도 바꿔야한다

<br>

```
"MYSQL_URL":"mysql+pymysql://root@localhost:3306/fastapi",
```

로 되어있는데, 배포용으로 바꿔준다.

<br>

```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install build-essential
sudo apt-get install curl git vim python3 python3-pip
touch .gitconfig
git config --global user.name ""
git config --global user.email ""
git config --global --list
git clone <프로젝트>
cd <프로젝트>
vi secrets.json
sudo pip install -r requirements.txt
sudo python3 server.py
```

추가적으로 light sail에 mysql을 깔아준다.  
로컬에서 테스트할 때는 로컬에 설치된 Mysql에서 연결했다. 근데 lightsail ubuntu는 mysql이 안깔려있다.  
전에는 rds를 연결해서 사용해서 aws ec2에 mysql을 설치할 필요가 없었지만, 지금은 그냥 하니까  
mysql을 설치해줘야한다.  

<br>

연결할때는 lightsail 인스턴스를 클릭하면 port가 나온다. localhost 대신 그 ip를 넣으면 된다.

<br>
