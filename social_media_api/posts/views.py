from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Like, Post
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    from django.contrib.contenttypes.models import ContentType  # Import for notification

    post = get_object_or_404(Post, pk=pk)

    if Like.objects.filter(user=request.user, post=post).exists():
        return Response({'message': 'You already liked this post.'}, status=400)

    like = Like.objects.create(user=request.user, post=post)

    # Create notification for post owner (if not the current user)
    if post.user != request.user:
        Notification.objects.create(
            recipient=post.user,
            actor=request.user,
            verb='liked your post',
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=post.pk
        )

    return Response({'message': 'Post liked successfully.'})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like = get_object_or_404(Like, user=request.user, post=post)
    like.delete()
    return Response({'message': 'Post unliked successfully.'})
