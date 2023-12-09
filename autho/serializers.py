from rest_framework import serializers
from autho.models import customers

class UserSerializer(serializers.ModelSerializer):
    customer_id = serializers.CharField(read_only=True)
    class Meta:
        model=customers
        fields = ('customer_id', 'first_name', 'middle_name', 'last_name', 'email', 'phone_number', 'password')

    def create(self, validated_data):
        customer = customers.create_customer(validated_data)
        return customer
    
    def update(self, instance, validated_data):
        instance.update(**validated_data)
        instance.save()
        return instance