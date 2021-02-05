from rest_framework import serializers
from .models import Employee, Company


class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response["company"] = CompanySerializer(instance.company).data
        return response
