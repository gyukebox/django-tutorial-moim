from django.urls import path
from moim.views import *

urlpatterns = [
    path('', IndexView.as_view()),
    # path('users/<uuid:user_id>/', UserDetailView.as_view()),
    path('moim/<uuid:moim_id>/', MoimDetailView.as_view()),
]