# aws iam, mfa 설정

- [iam 세팅한 블로깅](https://velog.io/@wlgns410/aws-iam)

<br>

직원 관리를 하는 권한은 aws에서 가장 큰 권한이다.  
이럴 때는 Administrator 권한을 준다.  
나머지 개발자는 직원관리는 불가능하지만, 모든 aws 서비스는 관리 가능하게 PowerUserAccess 권한을 주면 aws를 가지고 업무하는데 어려움이 없다.  

<br>

사실 베타 ~ 시리즈 B 정도 되는 회사에게 적합한 세팅방법이고, 직원의 업무가 세분화되면, iam 세팅의 권한을 더 쪼개줘야한다.  
하지만 아직 시드 단계이므로 이정도면 충분쓰.


<br>


![image](https://user-images.githubusercontent.com/81137234/168574263-1c34f844-d354-42b0-b98a-876fdcadf553.png)

<br>

root 계정을 mfa 세팅했다면, iam 계정도 mfa 2차 인증을 해야 aws 서비스에 엑세스가 가능해진다.  
이거 안하면 아무리 PowerUserAccess 든, Administrator든 설정해도 아무 소용없다. 


<br>
