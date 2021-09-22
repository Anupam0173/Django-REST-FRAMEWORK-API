
from django.urls import path
from django.urls.conf import include
from apibasic import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')
urlpatterns = [
    path('viewset/', include(router.urls)),
    path(r'api/', views.ArticleAPIView.as_view()),
    path(r'generic/', views.GenericAPIView.as_view()),
    path(r'gupdate/<int:pk>/', views.GenericAPIDetailView.as_view()),
    # path(r'gupdate/<int:pk>/', jwt_views.GenericAPIDetailView.as_view()),
    path('article/', views.articles_list),

]
