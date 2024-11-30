from django.urls import path
from .views import PublicListCreateView, CommentListCreateView, PublicListPutDeleteView, CommentListPutDeleteView

urlpatterns = [
    path('public_list_create/', PublicListCreateView.as_view(), name='public_list_create'),
    path('comment_list_create/', CommentListCreateView.as_view(), name='comment_list_create'),
    path('public_put_delete/', PublicListPutDeleteView.as_view(), name='public_put_delete'),
    path('comment_put_delete/', CommentListPutDeleteView.as_view(), name='comment_put_delete'),
]
