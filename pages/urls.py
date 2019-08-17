from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('create', views.create, name='create'),
    path('event/<int:event_id>', views.event, name='event'),
    path('visitor/<int:event_id>', views.visitor, name='visitor'),
]
