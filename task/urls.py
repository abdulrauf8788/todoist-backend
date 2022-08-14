from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', views.TaskViewSet, basename='tasks')

urlpatterns = router.urls
