# 디버그 사용법

계속 settings.py에 logging을 작성해서 logger를 봤었다.  
그러다가 debugging 툴을 써봐야하지않겠냐고 해서 간단하게 살펴봤다.  

<br>

매우 간단

<br>

<img width="1331" alt="스크린샷 2022-04-23 오후 1 56 33" src="https://user-images.githubusercontent.com/81137234/164878720-0647a6ae-d0e5-492a-8d86-06ef277ad268.png">

<br>

벌레모양 디버그 버튼을 누른다.  
그리고 Run and Debug 버튼을 누른다.  
어떤 언어/프레임워크로 할건지 고르라고 한다.  
Django를 골랐다.  
그러니까 manage.py runserver가 자동으로 되었다.  
debug = True으로 해놔야 돌아간다.  
그러고 breaking point를 지정한다.    
그럼 위처럼 debuging 된 결과가 나온다.  

<br>

자주 써봐야겠다.  

<br>
