from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


from .models import Employee, Company
from .serializers import CompanySerializer, EmployeeSerializer
# Create your views here.


class CompanyList(APIView):

    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeList(APIView):
    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        company = self.get_object(pk)
        user = Employee.objects.filter(pk=pk)
        # print(user.__dict__)
        for i in user:
            print(i.username)
            print(i.email)
            print(i.phone)

        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        # user = Employee.objects.filter(pk=pk)

        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
