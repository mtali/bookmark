from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),

    # include all athentication urls
    path('', include('django.contrib.auth.urls')),
]
