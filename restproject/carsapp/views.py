from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cars
from .serializer import CarsSerializer

# Create your views here.
class CarListView(APIView):
    def get(Self,request):
        cars=Cars.objects.all()
        serializer=CarsSerializer(cars, many=True)
        return Response(serializer.data)

class CarCreateView(APIView):   
    def post(Self,request):
        serializer=CarsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class CarDetailView(APIView):
    def get(self, request, pk):
        try:
            car = Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarsSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CarUpdateView(APIView):
    def put(self, request, pk):
        try:
            car = Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarsSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CarDeleteView(APIView):
    def delete(self, request, pk):
        try:
            car = Cars.objects.get(pk=pk)
        except Cars.DoesNotExist:
            return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response({'msg': 'Car deleted successfully'}, status=status.HTTP_200_OK)