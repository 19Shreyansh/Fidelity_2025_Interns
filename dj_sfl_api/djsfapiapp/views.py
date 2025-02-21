from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Trip
from .serializer import TripSerializer,TripDetailsSerializer

class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    
    @action(detail=False,methods=['get'])
    def by_date(self,request):
        date=request.query_params.get('trip_date',None)
        if date is not None:
            trips=Trip.objects.filter(trip_date=date)
            serializer=self.get_serializer(trips,many=True)
            return Response(serializer.data)
        else:
            return Response("Error")

class TripDetailViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripDetailsSerializer