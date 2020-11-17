from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'birthlot', views.BirthLotViewset)
router.register(r'rabbit', views.RabbitViewset)
router.register(r'disease', views.DiseaseViewset)
router.register(r'diagnosis', views.DiagnosisViewset)
router.register(r'sale', views.SaleViewset)
router.register(r'purchase', views.PurchaseViewset)


urlpatterns = [
    path('', include(router.urls)),

]