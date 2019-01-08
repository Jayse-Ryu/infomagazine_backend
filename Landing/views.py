from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .serializers import LandingSerializer, LayoutSerializer
from .models import Landing, Layout


class LandingViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     viewsets.GenericViewSet):
    queryset = Landing.objects.all().order_by('-created_date')
    serializer_class = LandingSerializer
    lookup_field = 'id'
    # print('Basic view queryset = ', queryset)

    def create(self, request, *args, **kwargs):
        # print('Create request = ', request)
        # print('Create args = ', args)
        # print('Create kwargs = ', kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, headers=headers)

    def list(self, request, *args, **kwargs):
        # print('List request = ', request)
        # print('List args = ', args)
        # print('List args = ', kwargs)
        queryset = self.filter_queryset(self.get_queryset())

        # If list searched as landing page name
        name = self.request.query_params.get('name', None)
        print('name catched? ', name)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
            print('name query catched? ', queryset)

        # If list searched as company name
        company = self.request.query_params.get('company', None)
        print('company name arg ', company)
        if company is not None:
            queryset = queryset.filter(company__name__icontains=company)
            print('company query ', queryset)

        # If list searched as manager name
        manager = self.request.query_params.get('manager', None)
        if manager is not None:
            queryset = queryset.filter(manager__full_name__icontains=manager)
            print('manager query ', queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        # print('Retrieve request = ', request)
        # print('Retrieve args = ', args)
        # print('Retrieve kwargs = ', kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        # print('Update request = ', request)
        # print('Update args = ', args)
        # print('Update kwargs = ', kwargs)
        partial = kwargs.pop('partial = ', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        # print('Delete instance = ', instance)
        instance.delete()


class LayoutViewSet(viewsets.ModelViewSet):
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer
