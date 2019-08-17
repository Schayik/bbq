from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('event/<int:event_id>', views.event, name='event'),
    path('visitor/<int:event_id>', views.visitor, name='visitor'),
    path('meat/<int:event_id>', views.meat, name='meat')
]
