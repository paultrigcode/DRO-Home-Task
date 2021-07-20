from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from . import views
from .views import CycleSettingViewSet,CycleEventViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'create-cycles',CycleSettingViewSet)
router.register(r'cycle_event',CycleEventViewSet)


urlpatterns = [
    re_path(r'', include(router.urls)),

]
