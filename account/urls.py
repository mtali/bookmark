from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),

    # registration urls
    path('register/', views.register, name='register'),

    # include all athentication urls
    path('', include('django.contrib.auth.urls')),
]
