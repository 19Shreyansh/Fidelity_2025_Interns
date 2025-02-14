from django.shortcuts import render
from .models import Question
from .serializer import QuestionSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response

# Create your views here.
class QuestionViewSet(viewsets.ViewSet):
    def list(self,request): #kind of alternative of Get but difference is List is evaluated but Get is not evaluated  kind of getall
        quest=Question.objects.all()
        serializer=QuestionSerializer(quest, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def retrieve(self,request,pk=None): #kind of alternative for getbyID 
        if pk is not None:
            quest=Question.objects.get(pk=pk)
            serializer=QuestionSerializer(quest)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'error':'Question not found'},status=status.HTTP_404_NOT_FOUND)

    def create(self,request):
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if pk is not None:
            quest=Question.objects.get(pk=pk)
            serializer=QuestionSerializer(quest,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Question not found'},status=status.HTTP_404_NOT_FOUND)

    def destroy(self,request,pk=None):
        if pk is not None:
            quest=Question.objects.get(pk=pk)
            quest.delete()
            return Response({'msg':'Question deleted successfully'},status=status.HTTP_200_OK)
        return Response({'error':'Question not found'},status=status.HTTP_404_NOT_FOUND)
