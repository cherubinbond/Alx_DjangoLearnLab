from django.urls import path, include
from .views import FeedView
from rest_framework.routers import DefaultRouter

# Initialize the router
router = DefaultRouter()

# Register the FeedView with the router
router.register(r'feed', FeedView, basename='feed')

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs
    # Additional explicit paths can be added here if necessary
]
