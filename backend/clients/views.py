from django.shortcuts import render

from django_filters import rest_framework as filters

from django.db.models import Q

from rest_framework import permissions, viewsets


# Create your views here.

from core.models import (
    Client, Attachment, ClinicalExamination, ClientHealthStatus
)
from .serializers import (
    AttachmentSerializer, ClientSerializer,
    ClinicalExaminationSerializer, ClientHealthStatusSerializer
)
from .pagination import ClientPagination


class AttachmentViewSet(viewsets.ModelViewSet):
    # Manage ingredientss in the database
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    lookup_field = 'id'

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        # print(self.request.query_params)
        queryset = Attachment.objects.all()
        client = self.request.query_params.get('client', None)
        type = self.request.query_params.get('type', None)

        if client is not None:
            queryset = queryset.filter(client=client)

        if type is not None:
            queryset = queryset.filter(file_type=type)

        return queryset.order_by('-id')

    def perform_create(self, serializer):
        """Create a new attachment"""
        print(self.request.user)
        serializer.save(user=self.request.user)


class AllClientsViewSet(viewsets.ModelViewSet):
    # Manage ingredientss in the database
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = None
    lookup_field = 'id'


class ClinicalExaminationViewset(viewsets.ModelViewSet):
    queryset = ClinicalExamination.objects.all()
    serializer_class = ClinicalExaminationSerializer
    lookup_field = 'client'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ClientViewSet(viewsets.ModelViewSet):
    # Manage ingredientss in the database
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    pagination_class = ClientPagination
    lookup_field = 'id'

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        # print(self.request.query_params)
        queryset = Client.objects.all()

        # PERFORM FILTER BY SEARCH INPUT
        conditions = Q()
        keywords = self.request.query_params.get('input', None)
        # print(keywords)
        if keywords:

            keywords_list = keywords.split(' ')
            print(keywords_list)
            for word in keywords_list:
                conditions |= Q(name__icontains=word) | Q(
                    email__icontains=word)

            if conditions:
                # print(type(conditions))
                queryset = Client.objects.filter(conditions)

        # PERFORM FILTER BY DATE
        # PATIENT OBJECT DOESNT HAVE DATE

        return queryset


class ClientHealthStatusViewSet(viewsets.ModelViewSet):
    queryset = ClientHealthStatus.objects.all()
    serializer_class = ClientHealthStatusSerializer
    lookup_field = 'client'
