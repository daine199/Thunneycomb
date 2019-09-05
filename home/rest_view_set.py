#! /usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAdminUser

from .models import Entrance, Switch
from .serializer import EntranceSerializer, SwithSerializer


# ViewSets define the view behavior.
@permission_classes([IsAdminUser])
class EntranceViewSet(viewsets.ModelViewSet):
    queryset = Entrance.objects.all()
    serializer_class = EntranceSerializer


@permission_classes([IsAdminUser])
class SwitchViewSet(viewsets.ModelViewSet):
    queryset = Switch.objects.all()
    serializer_class = SwithSerializer
