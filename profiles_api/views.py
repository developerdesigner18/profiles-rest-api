from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
#test purpose:-
class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            'hey! hows goin'
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})
