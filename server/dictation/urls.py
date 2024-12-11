from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter()
router.register('lesson', views.LessonViewSet, basename='lesson')

urlpatterns = [
    
] + router.urls
