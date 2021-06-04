from api.serializers import ImpactSerializer
from django.shortcuts import render
from rest_framework.mixins import (
  CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet
from .models import Impact
# Create your views here.

class ImpactViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin):
  serializer_class = ImpactSerializer
  queryset = Impact.objects.all()