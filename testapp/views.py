from django.shortcuts import render
from testapp.models import Employee
from testapp.serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView
from testapp.pagination import MyPagination,MyPagination2,MyPagination3

class EmployeeListView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    search_fields=('ename','eno')                  #searching using DRF
    search_fields=('^eno',)                        #starts with 
    # search_fields=('=eno',)                        #equal
    search_fields=('ename','eno') 
    ordering_fields=('eno','esal')                 #default value __all__
    # pagination_class=MyPagination3               #custom pagination class import from pagination.py
    """Plain vanilla searching"""
    # def get_queryset(self):
    #     name=self.request.GET.get('ename')
    #     if name is not None:
    #         qs=Employee.objects.filter(ename__icontains=name)
    #     return qs
