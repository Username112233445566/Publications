from django.urls import path
from .views import PublicView

urlpatterns = [
    path('public/', PublicView.as_view(), name='public'),
]
