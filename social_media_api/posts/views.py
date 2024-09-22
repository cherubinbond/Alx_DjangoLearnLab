from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post
from accounts.models import CustomUser
from .serializers import PostSerializer  # Ensure you have a serializer for your Post model

class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        # Get the current user
        current_user = self.request.user
        
        # Get the users that the current user is following
        following_users = current_user.following.all()
        
        # Filter posts by the followed users and order them by creation date
        return Post.objects.filter(author__in=following_users).order_by('-created_at')  # Adjust field as necessary
