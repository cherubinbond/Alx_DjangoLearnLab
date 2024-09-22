from django.urls import path
from . import views

urlpatterns = [
    path('feed/', views.get_feed, name='get_feed'),
    # Existing URL patterns...
]