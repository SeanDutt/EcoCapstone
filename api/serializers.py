from rest_framework.serializers import ModelSerializer
from .models import Impact

class ImpactSerializer(ModelSerializer):
  class Meta:
    model = Impact
    fields = (
      'id', 'item', 'description', 'co2PerUnit', 'category',
    )