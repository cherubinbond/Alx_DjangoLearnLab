# urls.py

from django.urls import path
from .views import LikeListCreateView, LikeRetrieveDestroyView

urlpatterns = [
    path('posts/<int:post_pk>/likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('posts/<int:post_pk>/likes/<int:pk>/', LikeRetrieveDestroyView.as_view(), name='like-retrieve-destroy'),
]