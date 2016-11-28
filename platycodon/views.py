from .serializers import PlaytcodonSerializer
from .models import Platycodon
from rest_framework import viewsets
# Create your views here.


class PlatycodonViewSet(viewsets.ModelViewSet):
    queryset = Platycodon.objects.all()
    serializer_class = PlaytcodonSerializer

