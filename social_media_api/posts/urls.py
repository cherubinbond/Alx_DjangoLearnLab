from django.urls import path, include
from .views import FeedView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'feed', FeedView, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
]
