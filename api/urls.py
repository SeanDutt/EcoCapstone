from django.conf.urls import include, re_path
from rest_framework.routers import DefaultRouter
from .views import ImpactViewSet
from django.urls import path
from . import views

router = DefaultRouter()
router.register("impacts", views.ImpactViewSet, basename='impacts')

urlpatterns = [
  re_path('^', include(router.urls)),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]