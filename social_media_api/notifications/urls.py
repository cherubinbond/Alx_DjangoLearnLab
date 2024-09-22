from django.urls import path
from .views import list_notifications

urlpatterns = [
    path('notifications/', list_notifications, name='list_notifications'),
]
