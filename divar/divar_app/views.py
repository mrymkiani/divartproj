from django.shortcuts import render
from .models import Advertisment
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView , RetrieveUpdateDestroyAPIView ,ListCreateAPIView 
from .serilize import AdverSerializer

class AdDetail(RetrieveUpdateDestroyAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdverSerializer
    
class AdModify(ListCreateAPIView):
    queryset = Advertisment.objects.all()
    serializer_class = AdverSerializer
    

# Create your views here.
