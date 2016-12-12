from .serializers import PlaytcodonSerializer
from .models import Platycodon
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required()
class PlatycodonViewSet(viewsets.ModelViewSet):
    queryset = Platycodon.objects.all()
    serializer_class = PlaytcodonSerializer

