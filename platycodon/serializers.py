from .models import Platycodon
from rest_framework import serializers


class PlaytcodonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Platycodon
        fields = ('id', 'title', 'content', 'update_time', 'create_time')
