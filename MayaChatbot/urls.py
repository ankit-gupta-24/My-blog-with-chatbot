from django.urls import path
from .views import MayaResponse
urlpatterns = [
    path('',MayaResponse,name='MayaResponse'),
]