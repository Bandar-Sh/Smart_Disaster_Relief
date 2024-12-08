from rest_framework.routers import DefaultRouter
from .views import DroneViewSet, LocationViewSet

router = DefaultRouter()
router.register(r'drone', DroneViewSet)
router.register(r'locations', LocationViewSet)

urlpatterns = router.urls

