from rest_framework import serializers

from .models import Mobil

class MobilSerializer(serializers.ModelSerializer):
  class Meta:
    model = Mobil
    fields = '__all__'