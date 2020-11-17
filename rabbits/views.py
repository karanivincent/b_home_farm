from django.shortcuts import render
from rest_framework import viewsets

from .models import BirthLot, Rabbit, Disease, Diagnosis, Sale, Purchase
# from .forms import RabbitForm, BirthLotForm, DiseaseForm, DiagnosisForm, SaleForm, PurchaseForm
from .serializers import (BirthLotSerializer, RabbitSerializer, DiseaseSerializer,
                          DiagnosisSerializer, SaleSerializer, PurchaseSerializer)

# from django.views.generic import (
#     CreateView, DetailView, UpdateView, DeleteView, ListView)


class BirthLotViewset(viewsets.ModelViewSet):
    queryset = BirthLot.objects.all()
    serializer_class = BirthLotSerializer


class RabbitViewset(viewsets.ModelViewSet):
    queryset = Rabbit.objects.all()
    serializer_class = RabbitSerializer


class DiseaseViewset(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer


class DiagnosisViewset(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosisSerializer


class SaleViewset(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class PurchaseViewset(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


######################################################################

# class BirthLotViewset(viewsets.ModelViewSet):
#     queryset = BirthLot.objects.all()
#     serializer_class = BirthLotSerializer


# class RabbitViewset(viewsets.ModelViewSet):
#     queryset = Rabbit.objects.all()
#     serializer_class = RabbitSerializer


# class DiseaseViewset(viewsets.ModelViewSet):
#     queryset = Disease.objects.all()
#     serializer_class = DiseaseSerializer


# class DiagnosisViewset(viewsets.ModelViewSet):
#     queryset = Diagnosis.objects.all()
#     serializer_class = DiagnosisSerializer


# class SaleViewset(viewsets.ModelViewSet):
#     queryset = Sale.objects.all()
#     serializer_class = SaleSerializer


# class PurchaseViewset(viewsets.ModelViewSet):
#     queryset = Purchase.objects.all()
#     serializer_class = PurchaseSerializer
