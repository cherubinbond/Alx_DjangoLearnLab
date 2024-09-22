from rest_framework import generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserRegistrationSerializer, UserLoginSerializer  # Ensure correct serializers are imported

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer  # Use the correct serializer for user registration

class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
            'email': user.email
        })

class FollowUserView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.add(user_to_follow)
        return Response({'message': f'You are now following {user_to_follow.username}'})

class UnfollowUserView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.following.remove(user_to_unfollow)
        return Response({'message': f'You have unfollowed {user_to_unfollow.username}'})
