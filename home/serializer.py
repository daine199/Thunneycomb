#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from .models import Entrance, Switch


# Serializers define the API representation.
class EntranceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entrance
        fields = ['entrance', 'entrance_url']


class SwithSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Switch
        fields = ['switch_key', 'switch_value']
