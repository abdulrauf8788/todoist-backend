from .permissions import HasApiKey
from .models import Task
from .serializers import TaskSerializer
from rest_framework import viewsets


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [HasApiKey] 

    def get_queryset(self):
        user_key = self.request.headers.get("User-Key")
        return Task.objects.filter(user_key=user_key)