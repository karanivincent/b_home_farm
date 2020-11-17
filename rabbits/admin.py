from django.contrib import admin
from .models import BirthLot, Rabbit, Disease, Diagnosis, Sale, Purchase

admin.site.site_header = 'Rabbits Manager'


class CustomAdmin(admin.ModelAdmin):
    # fields= ('time',)
    # exclude = ('time',)
    list_display = ('nameType', 'name')
    # list_filter = ('name', 'time')


admin.site.register(BirthLot)
admin.site.register(Rabbit)
admin.site.register(Disease)
admin.site.register(Diagnosis)
admin.site.register(Sale)
admin.site.register(Purchase)