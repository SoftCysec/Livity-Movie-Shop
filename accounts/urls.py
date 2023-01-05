from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.cancel_url, name='cancel_url'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
