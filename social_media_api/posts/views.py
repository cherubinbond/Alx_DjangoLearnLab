from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch the post using its primary key
    like, created = Like.objects.get_or_create(user=request.user, post=post)  # Create or get the Like instance

    if created:
        # Create notification for the post's author
        Notification.objects.create(
            recipient=post.author,  # Assuming Post model has an author field
            actor=request.user,
            verb='liked your post',
            target=post
        )
        return Response({'status': 'liked'}, status=status.HTTP_201_CREATED)
    
    return Response({'status': 'already liked'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)  # Fetch the post using its primary key
    try:
        like = Like.objects.get(user=request.user, post=post)  # Attempt to get the existing Like
        like.delete()  # Remove the Like
        return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)
    except Like.DoesNotExist:
        return Response({'status': 'not liked yet'}, status=status.HTTP_400_BAD_REQUEST)
