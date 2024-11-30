from django.urls import path
from .views import PublicView, CommentView

urlpatterns = [
    path('public/', PublicView.as_view(), name='public'),
    path('comment/', CommentView.as_view(), name='comment'),
]
