from django import forms
from .models import Rabbit, BirthLot, Disease, Diagnosis, Sale, Purchase


class RabbitForm(forms.ModelForm):

    class Meta():
        model = Rabbit
        fields = '__all__'


class BirthLotForm(forms.ModelForm):

    class Meta():
        model = BirthLot
        fields = '__all__'


class DiseaseForm(forms.ModelForm):

    class Meta():
        model = Disease
        fields = '__all__'


class DiagnosisForm(forms.ModelForm):

    class Meta():
        model = Diagnosis
        fields = '__all__'


class SaleForm(forms.ModelForm):

    class Meta():
        model = Sale
        fields = '__all__'


class PurchaseForm(forms.ModelForm):

    class Meta():
        model = Purchase
        fields = '__all__'
