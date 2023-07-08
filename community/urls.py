from django.contrib import admin
from django.urls import path, include
from board.views import *
from members.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('members/', include('members.urls')),
    path('board/', include('board.urls')),
    path('dj/', include('dj_rest_auth.urls')),
    path('dj/registration/', include('dj_rest_auth.registration.urls')),
]
