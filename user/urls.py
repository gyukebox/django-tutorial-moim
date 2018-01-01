from django.urls import path
from user.views import *

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('logout/', UserLogoutView.as_view()),
    path('register/', UserRegisterView.as_view()),
]
