'''
APPOINTMENT REFACTOR
NOTE:
Yes, you're correct. In order to prefetch related data and avoid the for-loop, you can add a SerializerMethodField to your AppointmentSerializer and use the select_related and prefetch_related methods to retrieve the related data in one query.

Here's an example of how you can do this:

class AppointmentSerializer(serializers.ModelSerializer):
    treatments = serializers.SerializerMethodField()
    prescriptions = serializers.SerializerMethodField()
    medications = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ('id', 'client', 'date', 'treatments', 'prescriptions', 'medications')

    def get_treatments(self, obj):
        return TreatmentSerializer(obj.treatment_set.all(), many=True).data

    def get_prescriptions(self, obj):
        prescriptions = obj.prescription_set.all()
        return PrescriptionSerializer(prescriptions, many=True, context={'request': self.context['request']}).data

    def get_medications(self, obj):
        medicationIds = [p.medication.id for p in obj.prescription_set.all()]
        return MedicationSerializer(Medication.objects.filter(id__in=medicationIds), many=True).data

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().select_related('client').prefetch_related('treatment_set', 'prescription_set', 'prescription_set__medication')



class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().prefetch_related('prescription_set', 'treatment_set')
    serializer_class = AppointmentSerializer
    pagination_class = AppointmentPagination
    lookup_field = 'id'
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AppointmentFilter

    def perform_create(self, serializer):
        """Create a new appointment"""
        serializer.save(user=self.request.user)


class MedicationViewset(viewsets.ModelViewSet):
    queryset = Medication.objects.all().select_related('prescription')
    serializer_class = MedicationSerializer
    lookup_field = 'id'
    kwargs_fields = 'medicine_name'
    filter_backends = [MedicationIdFilter]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
'''

'''
class AppointmentSerializer(serializers.ModelSerializer):
    # Serializer for uploading images for recipes
    
    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    startDate = serializers.SerializerMethodField()
    endDate = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ('id', 'client', 'description', 'date',
                  'date_to', 'start', 'end', 'startDate', 'endDate',
                  )
        read_only_Fields = ('id',)
        not_required_fields = ('notes', 'prescription',)

    def get_start(self, obj):
        return f"{obj.date.strftime('%Y-%m-%d')} {obj.date.strftime('%H:%M')}"

    def get_end(self, obj):
        return f"{obj.date_to.strftime('%Y-%m-%d')} {obj.date_to.strftime('%H:%M')}"

    def get_startDate(self, obj):
        return obj.date

    def get_endDate(self, obj):
        return obj.date_to

'''


'''
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

    

    def get_queryset(self):
        queryset = self.filter_by_month()
        queryset = self.filter_by_keywords(queryset)
        queryset = self.filter_by_date(queryset)
        queryset = self.filter_by_client(queryset)
        return queryset
'''
