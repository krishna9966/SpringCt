from rest_framework import serializers
from .models import Employee, Company


class CompanySerializer(serializers.ModelSerializer):
    # users = serializers.StringRelatedField(many=True)
    class Meta:
        model = Company
        fields = ['companyname', 'city']
# class Companyrelated(serializers.RelatedField):
#     def to_representation(self, value):
#         users = EmployeeSerializer()
#         return super().to_representation(value)

class EmployeeSerializer(serializers.ModelSerializer):
    # company = CompanySerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        # fields = ['username', 'company', 'email', 'phone']
        fields = '__all__'
