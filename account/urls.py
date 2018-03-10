from django.urls import path
from django.contrib.auth.views import (
    login, logout, logout_then_login,
    password_change, password_change_done
)

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('logout-then-login/', logout_then_login, name='logout_then_login'),

    # change password urls
    path('password-change/', password_change, name='password_change'),
    path('password-change/done/', password_change_done, name='password_change_done'),
]
