from rest_framework.routers import DefaultRouter
from .views import RealTimeDataViewSet

router = DefaultRouter()
router.register(r'realtime-data', RealTimeDataViewSet)

urlpatterns = router.urls
