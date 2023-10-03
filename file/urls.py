from django.urls import path
from .views import *

urlpatterns = [
    path('', FileListCreateApiView.as_view()),
    path('<int:pk>', FileRetrieveUpdateDestroyApiView.as_view()),
]
