from rest_framework import viewsets, mixins
from rest_framework.response import Response
from .models import Collection
from .serializers import CollectionSerializer
# from django.db.models import Q
from django.utils import timezone
from datetime import timedelta, date, datetime


class CollectionViewSet(mixins.CreateModelMixin,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):
    queryset = Collection.objects.all().order_by('-created_date')
    serializer_class = CollectionSerializer
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
        queryset = self.filter_queryset(self.get_queryset())

        # Filter needed
        # Landing_id = int,
        # Form_group = int,
        # Quick_filter = datetime,
        # Datetime = datetime,

        # Landing id filter
        landing = self.request.query_params.get('landing', None)
        if landing is not None:
            print('Landing id is? ', landing)
            queryset = queryset.filter(landing_id=landing)

        # Form group filter
        form = self.request.query_params.get('form', None)
        if form is not None:
            print('Form id is? ', form)
            queryset = queryset.filter(form_group_id=form)

        # Quick date filtered
        quick = self.request.query_params.get('quick', None)
        if quick is not None:
            if quick in 'lastmonth':
                first_day_of_current_month = timezone.now().replace(day=1)
                last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
                calc_year = last_day_of_previous_month.year
                calc_month = last_day_of_previous_month.month
                calc_day = last_day_of_previous_month.day
                print('Last month result', calc_year, calc_month, calc_day)
                queryset = queryset.filter(created_date__gte=date(calc_year, calc_month, 1),
                                           created_date__lte=date(calc_year, calc_month, calc_day))
            elif quick in 'thismonth':
                last_day_of_current_month = (timezone.now().replace(day=1) + timedelta(days=32))\
                                                .replace(day=1) - timedelta(days=1)
                calc_year = last_day_of_current_month.year
                calc_month = last_day_of_current_month.month
                calc_day = last_day_of_current_month.day
                print('The last day of this month result', calc_year, calc_month, calc_day)
                queryset = queryset.filter(created_date__gte=date(calc_year, calc_month, 1),
                                           created_date__lte=date(calc_year, calc_month, calc_day))
            elif quick in 'recent3':
                now = timezone.now()
                delta = timedelta(days=3)
                calc_date = (now - delta)
                print('Recent 3 days date', calc_date)
                queryset = queryset.filter(created_date__gte=calc_date,
                                           created_date__lt=date(now.year, now.month, now.day))
            elif quick in 'recent2':
                now = timezone.now()
                delta = timedelta(days=2)
                calc_date = (now - delta)
                print('Recent 2 days date', calc_date)
                queryset = queryset.filter(created_date__gte=calc_date,
                                           created_date__lt=date(now.year, now.month, now.day))
            elif quick in 'yesterday':
                now = timezone.now()
                delta = timedelta(days=1)
                calc_date = (now - delta)
                print('Yesterday is ', calc_date)
                queryset = queryset.filter(created_date__gte=calc_date,
                                           created_date__lt=date(now.year, now.month, now.day))
            elif quick in 'today':
                now = timezone.now()
                print('Get today date ', now)
                queryset = queryset.filter(created_date__gte=date(now.year, now.month, now.day))

        # Get date picker filter
        # ex) 2019-01-08(T18:09:27.759556)
        start = self.request.query_params.get('start', None)
        end = self.request.query_params.get('end', None)
        if start is not None:
            try:
                datetime.strptime(start, '%Y-%m-%d')
                if end is not None:
                    try:
                        datetime.strptime(end, '%Y-%m-%d')
                        print('Date picker filtered')
                        print('Start date? ', start[:4], start[5:7], start[8:])
                        print('End date? ', end[:4], end[5:7], end[8:])
                        queryset = queryset.filter(created_date__gte=date(int(start[:4]), int(start[5:7]), int(start[8:])),
                                                   created_date__lte=date(int(end[:4]), int(end[5:7]), int(end[8:])))
                    except ValueError:
                        raise ValueError("Incorrect data format, 'End' should be YYYY-MM-DD")
            except ValueError:
                raise ValueError("Incorrect data format, 'Start' should be YYYY-MM-DD")

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