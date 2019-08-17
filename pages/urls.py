from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('event/<int:event_id>', views.event, name='event'),
    path('visitor/<int:event_id>', views.visitor, name='visitor'),
]
