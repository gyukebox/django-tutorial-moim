from django.urls import path
from moim.views import *

urlpatterns = [
    path('', MoimView.as_view()),
    path('<int:moim_id>/', MoimDetailView.as_view()),
    path('<int:moim_id>/apply/', MoimApplyView.as_view())
]
