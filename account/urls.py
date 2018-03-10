from django.urls import path
from django.contrib.auth.views import login, logout, logout_then_login


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout_then_login/', logout_then_login, name='logout_then_login'),
]