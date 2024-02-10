from django_filters import rest_framework as filters
from .models import Alert


class AlertFilter(filters.FilterSet):
    status = filters.CharFilter(field_name='status', lookup_expr='exact')

    class Meta:
        model = Alert
        fields = ['status']
