from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('signup/', views.signup),
    path('add_task/', views.add_task),
]