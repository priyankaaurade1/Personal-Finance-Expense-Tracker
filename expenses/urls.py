from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',view=dashboard, name='dashboard'),
    path('add/',view=add_expense, name='add_expense'),

    path('register/', view=register_view, name='register'),
    path('login/', view=login_view, name='login'),
    path('logout/', view=logout_view, name='logout'),
]
