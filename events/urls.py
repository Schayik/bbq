from django.urls import path

from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('create_event', views.create_event, name='create_event'),
    path('event/<int:event_id>', views.event, name='event'),
    path('create_meat/<int:event_id>', views.create_meat, name='create_meat'),
    path('visitor/<int:event_id>', views.visitor, name='visitor'),
    path('create_visitor/<int:event_id>',
         views.create_visitor, name='create_visitor')

]
