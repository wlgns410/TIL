from .models import Article
from .serializers import ArticleSerializer


#class기반 가장 기본인 apiview
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated # 쓰고 읽기 다 가능


#  근데 이건 list를 볼 수 없는것 같음. 무조건 url이 id를 다 입력하라는 것 같음
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    serializer_class = ArticleSerializer # 시리얼라이즈화도 이게 대신해줌 필요한건 오버라이드함
    queryset = Article.objects.all() # get_object를 이게 대신해줌
    lookup_field = 'id' # generic view는 pk를 default로 쓰는데, 파라미터를 바꾸려면 lookup_field를 써줘야함
    authentication_classes = [TokenAuthentication] #BasicAuthentication : username, email 등, SessionAuthentication:세션, TokenAuthentication: token
    permission_classes = [IsAuthenticated]

    def get(self, request, id =None):

        if id: 
            return self.retrieve(request) # 파라미터로 id가 있으면 detail
        else:
            return self.list(request) # list라는 메서드를 호출하면 list가 반환됨

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.delete(request, id)

