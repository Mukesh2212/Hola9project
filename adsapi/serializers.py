from rest_framework import serializers
from .models import  Product , WishListItems,BusinessProfile
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def update(self, instance, validated_data):
        # Handle partial updates
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

 #Wishlist Serializers

class WishListItemsTestSerializer(serializers.ModelSerializer):    
    class Meta:
        model = WishListItems
        fields = ['id','item']
        depth = 2  


class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = '__all__'
    def update(self, instance, validated_data):
        # Handle partial updates
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

# class EmployeeLogin2Serializer2(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeLogin2
#         fields = '__all__'

# class AssignTaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AssignTask
#         fields = '__all__'