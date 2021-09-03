from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
# app_name = 'users_api'

urlpatterns = [
    path("", views.homepage, name='homepage'),
    # path("login", views.login, name="login")
    path('login/', auth_views.LoginView.as_view(template_name='df/login.html'), name='login'),
    path('create_data/', views.create_data, name='create_data'),
    path('processing_data/', views.processing_data, name='processing_data'),
    path('export/', views.export, name='export')
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
