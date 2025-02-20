from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from restapp.serializer import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from restapp.models import Student
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.schemas import get_schema_view
# Create your views here.

@api_view(['POST'])
def postdata(request):
    std=StudentSerializer(data=request.data)
    if(std.is_valid()):
        std.save()
        return Response(std.data,status=status.HTTP_201_CREATED)
        # return Response("Student Created")
    return Response(std.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getall(request):
    std=Student.objects.all()
    serializer=StudentSerializer(std,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getbyid(request,pk):
    try:
        std=Student.objects.get(id=pk)
        serializer=StudentSerializer(std)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({'error':'Student Not Found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT']) #it id for updating the data
def update(request,pk):
    try:
        std=Student.objects.get(id=pk)
        serializer=StudentSerializer(std,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Student.DoesNotExist:
        return Response({'error':'Student Not Found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteid(request,pk):
    try:
        std=Student.objects.get(id=pk)
        std.delete()
        return Response({'msg':'Student Deleted'})
    except Student.DoesNotExist:
        return Response({'error':'Student Not Found'},status=status.HTTP_404_NOT_FOUND)
    


    
