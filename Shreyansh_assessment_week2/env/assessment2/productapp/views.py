from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from productapp.serializer import ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from productapp.models import Product
import json
# Create your views here.

@api_view(['POST'])
def postdata(request):
    prd=ProductSerializer(data=request.data)
    if(prd.is_valid()):
        prd.save()
        return Response(prd.data,status=status.HTTP_201_CREATED)
    return Response(prd.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getall(request):
    prd=Product.objects.all()
    if not prd:
        res={}
    else:
        serializer=ProductSerializer(prd,many=True)
        res=serializer.data
    with open('result.py','w') as f:
        f.write(f"result = {json.dumps(res,indent=4)}")
    return Response(res)


@api_view(['GET'])
def getbyid(request,pk):
    try:
        prd=Product.objects.get(id=pk)
        serializer=ProductSerializer(prd)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response({'error':'Product Not Found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT']) #it id for updating the data
def update(request,pk):
    try:
        prd=Product.objects.get(id=pk)
        serializer=ProductSerializer(prd,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Product.DoesNotExist:
        return Response({'error':'Product Not Found'},status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def deleteid(request,pk):
    try:
        prd=Product.objects.get(id=pk)
        prd.delete()
        return Response({'msg':'Product Deleted'})
    except Product.DoesNotExist:
        return Response({'error':'Product Not Found'},status=status.HTTP_404_NOT_FOUND)
    


    
