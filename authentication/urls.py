from django.urls import path
from .views import *

urlpatterns = [
    path('', UserRegistrationApiView.as_view()),
    path('list', UserListApiView.as_view()),
    path('check', CheckUsernameView.as_view()),
    path('<pk>', SingleUserApiView.as_view()),
]
