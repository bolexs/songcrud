from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SongViewSet


router = DefaultRouter()
router.register(r'songs', SongViewSet, basename='songs')

urlpatterns = [

] + router.urls