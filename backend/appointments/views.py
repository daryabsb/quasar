
from rest_framework import permissions, viewsets
from datetime import datetime, timedelta, date as dt
from .filters import (datefilter, get_date_range as delta,
                      MedicationIdFilter, AppointmentFilter)
from core.models import (
    Client, Prescription, Appointment,
    Treatment, Medication
)
from .serializers import (
    AppointmentSerializer, MedicationSerializer,
    PrescriptionSerializer, TreatmentSerializer,
)
from .pagination import AppointmentPagination


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    filter_class = AppointmentFilter

    def filter_by_month(self):
        month_name = self.request.query_params.get('month', None)
        if month_name:
            month = datetime.strptime(month_name.split()[0], '%B').month
            year = int(month_name.split()[1])
            month_start = datetime.strptime(
                f'{year}-{month:02d}-01', '%Y-%m-%d')
            if month == 12:
                next_month = 1
                next_year = year + 1
            else:
                next_month = month + 1
                next_year = year
            month_end = datetime.strptime(
                f'{next_year}-{next_month:02d}-01', '%Y-%m-%d') - timedelta(days=1)
            return Appointment.objects.filter(date__gte=month_start, date__lte=month_end)
        return Appointment.objects.all()

    def filter_by_date(self, queryset):
        today = datetime.now()
        date_query = self.request.query_params.get('dq', None)
        if date_query is not None:
            todays_date = dt.today()
            todays_query = datetime.strptime(
                f'{todays_date}T00:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
            query = delta(date_query)
            if query is not None:
                queryset = queryset.filter(
                    date__gte=todays_query, date__lte=query)
            if date_query == 'custom':
                date_str = self.request.query_params.get('date', None)
                if date_str is not None:
                    date = datetime.strptime(
                        f'{date_str}T00:00:00Z', '%Y-%m-%dT%H:%M:%SZ')
                    end_date = datetime.strptime(
                        f'{date_str}T23:59:00Z', '%Y-%m-%dT%H:%M:%SZ')
                    queryset = queryset.filter(
                        date__gte=date, date__lte=end_date)
        return queryset

    def filter_by_keywords(self, queryset):
        keywords = self.request.query_params.get('input', None)
        if keywords:
            conditions = Q()
            keywords_list = keywords.split(' ')
            for word in keywords_list:
                conditions |= Q(client__name__icontains=word) | Q(
                    description__icontains=word)
            if conditions:
                return queryset.filter(conditions)
        return queryset

    def filter_by_client(self, queryset):
        client_query = self.request.query_params.get('p', None)
        if client_query is not None:
            queryset = queryset.filter(client=client_query)
        return queryset

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_by_month()
        queryset = self.filter_by_keywords(queryset)
        queryset = self.filter_by_date(queryset)
        queryset = self.filter_by_client(queryset)
        return queryset.filter()


class PrescriptionViewset(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer
    lookup_field = 'appointment'

    def perform_create(self, serializer):
        appointment = serializer.validated_data['appointment']
        client = Client.objects.get(id=appointment.client.id)
        serializer.save(user=self.request.user, client=client)


class TreatmentViewset(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer
    lookup_field = 'appointment'

    def perform_create(self, serializer):
        appointment = serializer.validated_data['appointment']
        client = Client.objects.get(id=appointment.client.id)
        serializer.save(user=self.request.user, client=client)


class MedicationViewset(viewsets.ModelViewSet):
    queryset = Medication.objects.all().prefetch_related('prescriptions')
    serializer_class = MedicationSerializer
    lookup_field = 'id'
    kwargs_fields = 'medicine_name'
    filter_backends = [MedicationIdFilter]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
