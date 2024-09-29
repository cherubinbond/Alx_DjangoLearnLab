from django.shortcuts import get_object_or_404
from rest_framework import status, generics  # Importing generics for generic views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated  # Permission to ensure user is authenticated
from rest_framework.response import Response
from .models import Post, Like  # Ensure Post and Like models are imported correctly
from notifications.models import Notification
from .serializers import LikeSerializer  # Assuming you have a serializer for Like model

class LikeListCreateView(generics.ListCreateAPIView):
    """
    View to list and create likes.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])  # Get the post using the post_pk from URL
        like, created = serializer.save(user=self.request.user, post=post)  # Save the like instance

        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb='liked your post',
                target=post
            )

class LikeRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    """
    View to retrieve or delete a like.
    """
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get_object(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])  # Get the post using the post_pk from URL
        return get_object_or_404(Like, user=self.request.user, post=post)  # Get the like instance

# Note: You would need to set up your URLs to point to these views correctly.