from datetime import datetime, timedelta, date
from core.models import Appointment
from rest_framework import filters
import django_filters


class AppointmentFilter(django_filters.FilterSet):
    client = django_filters.NumberFilter(
        field_name='client', lookup_expr='exact')
    date = django_filters.DateFromToRangeFilter(field_name='date')
    description = django_filters.CharFilter(
        field_name='description', lookup_expr='icontains')
    client_name = django_filters.CharFilter(
        field_name='client__name', lookup_expr='icontains')

    class Meta:
        model = Appointment
        fields = {
            'client': ['exact'],
            # 'date': ['iexact'],
            'date': ['gte', 'lte'],
            'description': ['icontains'],
            # 'client_name': ['icontains'],
        }


class MedicationIdFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        medication_ids = request.query_params.getlist('id__in')
        if medication_ids:
            medication_ids = [int(id) for id in medication_ids[0].split(',')]
            queryset = queryset.filter(id__in=medication_ids)
        return queryset


class AdvanceFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')
        category = request.query_params.get('category')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        if category:
            queryset = queryset.filter(category=category)
        return queryset


# DATE FILTER GENERATOR
def get_date_range(date_query):

    aday = timedelta(days=2)
    week = timedelta(weeks=1)
    month = timedelta(days=30)
    today = date.today()
    tomorrow = today + aday
    now = datetime.now()

    # print(aday)

    return {
        'today': lambda: today,
        'tomorrow': lambda: tomorrow,
        'week': lambda: today + week,
        'month': lambda: today + month
    }.get(date_query, lambda: None)()


def datefilter(a, c):

    def myfilter(x):
        return a < x < c
    return myfilter
