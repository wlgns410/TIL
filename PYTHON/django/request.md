# request
올만에 보니 많이 까먹어서 다시 복습

## python request

> request.get('key', none)
전달 받은 dict의 key가 있다면 value를 리턴

## django request
이것은 django의 문법

<br>

### if method == GET
django는 메서드 요청을 분명히 알린다.  
보통 받을 때 사용, listview, detailview 등

<br>

> request.GET()
request의 모든 GET
전달 받은 모든 요청을 dict 형태로 return

> reuqest.GET.get('key', None) 

전달 받은 모든 요청인 dict의 value 값을 return

<br>

### if method == POST
보통 createview, updateview 등에서 사용

> request.POST()
request의 모든 POST 값을 dict 형태로 반환

> request.POST.get('key', None)
request의 모든 POST 값을 key가 있다면 value return

<br>

## django queryset api 에서 kwarg[]




```
django 공식 문서의 Queryset API 부분을 보면

filter(**kwagrs)
exclude(**kwagrs)
annotate(*args, **kwagrs)
get(**kwagrs)
create(**kwagrs)
get_or_create(defaults=None, **kwargs
update_or_create(defaults=None, **kwargs)
aggregate(*args, **kwargs)
update(**kwargs)
```
model manager method에서 **kwargs를 사용 한다.

```
def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk']) 

```

이말은 즉, key:value로 된 dict에서 pk라는 key 값의 value를 찾겠다.  
라는 뜻이다.

<br>

오랜만에 보니까 헷갈려서 다시 복습

<br>
