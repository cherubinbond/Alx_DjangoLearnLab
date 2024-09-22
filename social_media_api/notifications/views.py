from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Notification

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_notifications(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    serialized_notifications = [{'actor': n.actor.username, 'verb': n.verb, 'timestamp': n.timestamp} for n in notifications]
    return Response(serialized_notifications)
