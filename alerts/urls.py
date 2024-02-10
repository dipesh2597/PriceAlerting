from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AlertViewSet

router = DefaultRouter()
router.register(r'alerts', AlertViewSet, 'alert')

urlpatterns = router.urls
