from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename="article")

app_name = 'app1'

urlpatterns = [
   path('viewset/', include(router.urls)),
   # path('article/',article_list),
   # path('detail/<int:pk>',article_detail),
   path('article/',ArticleAPIView.as_view()),
   path('detail/<int:id>',ArticleDetails.as_view()),
   path('generic/article/<int:id>/',GenericAPIView.as_view()),
]