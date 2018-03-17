from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),

    # registration urls
    path('register/', views.register, name='register'),

    # user and profile update urls
    path('edit/', views.edit, name='edit'),

    # users listing and detail view
    path('users/', views.user_list, name='user_list'),
    re_path(r'^users/(?P<username>[-\w]+)/$', views.user_detail, name='user_detail'),

    # include all athentication urls
    path('', include('django.contrib.auth.urls')),
]
