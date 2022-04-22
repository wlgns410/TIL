from django.urls import path, include
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', ArticleViewSet, basename='articles')

urlpatterns = [
    # path('articles/', article_list),
    # path('detail/<int:pk>/', article_detial),

    # path('articles/', ArticleAPIView.as_view()),
    # path('detail/<int:id>/', ArticleDetails.as_view())


    # viewset & generic viewset
    path('viewset/', include(router.urls)),# 주소는 127.0.0.1:8000/viewset/article/ 이됨
    path('viewset/<int:pk>/', include(router.urls)),# 주소는 127.0.0.1:8000/viewset/article/5/ 이됨
]