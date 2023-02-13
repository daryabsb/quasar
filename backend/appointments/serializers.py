from rest_framework import serializers
from core.models import (
    Appointment, Prescription, Treatment, Medication,
)


class PrescriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prescription
        fields = [
            'id', 'appointment', 'medication', 'created'
        ]
        read_only_Fields = ('id', 'created',)


class TreatmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Treatment
        fields = [
            'id', 'appointment', 'note', 'created'
        ]
        read_only_Fields = ('id', 'created',)


class MedicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Medication
        fields = '__all__'
        read_only_Fields = ('id', 'created',)


class AppointmentSerializer(serializers.ModelSerializer):
    treatments = serializers.SerializerMethodField()
    prescriptions = serializers.SerializerMethodField()
    medications = serializers.SerializerMethodField()

    start = serializers.SerializerMethodField()
    end = serializers.SerializerMethodField()
    startDate = serializers.SerializerMethodField()
    endDate = serializers.SerializerMethodField()

    class Meta:
        model = Appointment
        fields = ('id', 'client', 'date', 'date_to', 'start', 'end', 'startDate', 'endDate',
                  'treatments', 'prescriptions', 'medications')

    def get_treatments(self, obj):
        return TreatmentSerializer(obj.treatments.all(), many=True).data

    def get_prescriptions(self, obj):
        prescriptions = obj.prescriptions.all()
        return PrescriptionSerializer(prescriptions, many=True, context={'request': self.context['request']}).data

    def get_medications(self, obj):
        medicationIds = [p.medication.id for p in obj.prescriptions.all()]
        return MedicationSerializer(Medication.objects.filter(id__in=medicationIds), many=True).data

    def get_start(self, obj):
        return f"{obj.date.strftime('%Y-%m-%d')} {obj.date.strftime('%H:%M')}"

    def get_end(self, obj):
        return f"{obj.date_to.strftime('%Y-%m-%d')} {obj.date_to.strftime('%H:%M')}"

    def get_startDate(self, obj):
        return obj.date

    def get_endDate(self, obj):
        return obj.date_to
