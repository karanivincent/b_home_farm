from rest_framework import serializers

from .models import BirthLot, Rabbit, Disease, Diagnosis, Sale, Purchase


class BirthLotSerializer(serializers.ModelSerializer):

    class Meta:
        model = BirthLot
        fields = '__all__'


class RabbitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rabbit
        fields = '__all__'

class DiseaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Disease
        fields = '__all__'

class DiagnosisSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Diagnosis
        fields = '__all__'        

class SaleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sale
        fields = '__all__'        

class PurchaseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Purchase
        fields = '__all__'        