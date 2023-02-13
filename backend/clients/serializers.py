from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers
from core.models import (
    Client, Attachment, ClinicalExamination, ClientHealthStatus
)


class AttachmentSerializer(serializers.ModelSerializer):
    # Serializer for uploading images for recipes

    class Meta:
        model = Attachment
        fields = ('id', 'client', 'file_type',
                  'filename', 'file', 'page_count')
        read_only_Fields = ('id', 'page_count')


class ClinicalExaminationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClinicalExamination
        fields = '__all__'
        read_only_Fields = ('id', 'created',)


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = [
            'id', 'name', 'dob', 'age', 'gender', 'description', 'phone',
            'email', 'image', 'status',
            # 'treatments', 'appointments', 'attachments',
            # 'examinations','medicals',

        ]
        read_only_Fields = ('id',)
        not_required_fields = ('age')


class ClientHealthStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientHealthStatus
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.heart_condition = validated_data.get(
            'heart_condition', instance.heart_condition)
        instance.blood_sugar = validated_data.get(
            'blood_sugar', instance.blood_sugar)
        instance.blood_pressure = validated_data.get(
            'blood_pressure', instance.blood_pressure)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)
        instance.smoking_status = validated_data.get(
            'smoking_status', instance.smoking_status)
        instance.alcohol_consumption = validated_data.get(
            'alcohol_consumption', instance.alcohol_consumption)
        instance.physical_activity = validated_data.get(
            'physical_activity', instance.physical_activity)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.save()
        return instance
