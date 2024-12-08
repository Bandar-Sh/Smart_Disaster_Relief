from rest_framework.routers import DefaultRouter
from .views import AudioDataViewSet

router = DefaultRouter()
router.register(r'audio', AudioDataViewSet)

urlpatterns = router.urls
