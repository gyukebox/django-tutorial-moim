from django.contrib import admin
from django.urls import path, include
from moim.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('users/', include('user.urls')),
    path('moim/', include('moim.urls')),
]
