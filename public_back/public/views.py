from .models import Public
from .serializers import PublicSerializer
from rest_framework import generics

class PublicView(generics.ListCreateAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer