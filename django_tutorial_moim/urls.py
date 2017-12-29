from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', IndexView.as_view()),
    path('users/', include('user.urls')),
    path('moim/', include('moim.urls')),
]
