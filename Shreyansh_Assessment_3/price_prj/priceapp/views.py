from rest_framework import viewsets
from .models import Price
from .serializer import PriceSerializer
import requests 
from rest_framework.response import Response

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

    def list(self,request):
        prices=Price.objects.all()
        price_serializer=PriceSerializer(prices,many=True)
        location_response = requests.get('http://127.0.0.1:8000/api/locations/')
        if location_response.status_code==200:
            location_data=location_response.json()
        else:
            location_data=[]

        data={
            'prices':price_serializer.data,
            'locations':location_data
        }
        return Response(data)