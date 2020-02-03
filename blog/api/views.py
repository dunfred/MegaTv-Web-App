from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView

from django.http import JsonResponse
from .serializer import CommentSerializer
from blog.models import Post, Comment

class CommentListView(ListAPIView):    
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ApiForAllCommentsView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Comment.objects.all()
        serializer = CommentSerializer(qs, many=True) 

        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)


class ApiForPostCommentsView(APIView):
    def get(self, request, post):
        qs = Comment.objects.filter(post=post)
        serializer = CommentSerializer(qs, many=True)
        
        return Response(data=serializer.data)