from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.views import APIView

from django.http import JsonResponse
from .serializer import CommentSerializer
from blog.models import Post, Comment, Author
from django.shortcuts import get_object_or_404


class ApiForAllCommentsView(APIView):
    def get(self, request, *args, **kwargs):
        qs = Comment.objects.all()
        serializer = CommentSerializer(qs, many=True)        
        
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        qr = dict(request.data)
        
        author = Author.objects.filter(author=qr['author'])

        if len(author) == 1:
            qr['author_id']     = int(author[0].id)
        else:
            new_author = Author(author=qr['author'])
            new_author.save()
            qr['author_id'] = int(new_author.id)
        
        qr['author']       = qr['author'][0]
        qr['body']       = qr['body'][0]
        qr['post']       = int(qr['post'][0])
        
        serializer = CommentSerializer(data=qr)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

