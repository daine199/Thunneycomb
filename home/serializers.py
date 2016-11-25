from .models import Entrance
from rest_framework import serializers


class EntranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrance
        fields = ('id', 'entrance', 'entrance_url')
