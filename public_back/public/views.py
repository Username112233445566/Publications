from .models import Public, Comment
from .serializers import PublicSerializer, CommentSerializer
from rest_framework import generics


class PublicView(generics.ListCreateAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer

    
class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer