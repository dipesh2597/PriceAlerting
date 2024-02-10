from rest_framework import viewsets, status
from django.core.cache import cache
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters import rest_framework as filters
from django.conf import settings
from .filters import AlertFilter
from .models import Alert
from .pagination import AlertViewPagination
from .serializers import AlertSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class AlertViewSet(viewsets.ModelViewSet):
    serializer_class = AlertSerializer
    filterset_class = AlertFilter
    pagination_class = AlertViewPagination
    filter_backends = [filters.DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['status']
    search_fields = ['coin_name', 'status']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Alert.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = cache.get('Alert')
        if not queryset:
            queryset = self.get_queryset()
            cache.set('Alert', queryset, timeout=settings.CACHE_TIMEOUT)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        print("save called", self.request, self.request.user)
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.status = 'DELETED'
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
