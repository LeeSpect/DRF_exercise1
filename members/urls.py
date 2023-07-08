from django.urls import path
from .views import *

app_name = 'members'

urlpatterns = [
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('signup/', Signup.as_view()),
]