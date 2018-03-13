from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),

    # registration urls
    path('register/', views.register, name='register'),

    # user and profile update urls
    path('edit/', views.edit, name='edit'),

    # include all athentication urls
    path('', include('django.contrib.auth.urls')),
]
