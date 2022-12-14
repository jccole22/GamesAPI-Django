from posixpath import basename
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('games', views.GameView)

urlpatterns = [
    path('', include(router.urls))
]