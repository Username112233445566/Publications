from .models import Public, Comment
from .serializers import PublicSerializer, CommentSerializer
from rest_framework import generics


class PublicListCreateView(generics.ListCreateAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer


class PublicListPutDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
   

class CommentListPutDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer