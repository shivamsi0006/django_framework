from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from profiles_api import models
from rest_framework import viewsets


class HelloApiView(APIView):

    serializer_class =serializers.HelloSerializer

    def get(self,request,format=None):

        an_apiview=[

            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'HEllo!','an_apiview':an_apiview})
    def post(self,request):
        serializers=self.serializer_class(data=request.data)

        if serializers.is_valid():
            name=serializers.validated_data.get('name')

            message=f'{name}'
            return Response({'message':message})
        else:
            return Response(serializers.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )
    def put(self,request,pk=None):
        return Response({"method":'PUT'})
    

    def patch(self,request,pk=None):
        return Response({"method":"PATCH"})
    
    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})
        



class HelloVIewSet(viewsets.ViewSet):

    serializers_class=serializers.HelloSerializer
    def list(self,request):

        a_viewset=[
            'Uses actions (list create,retrive ,update ,partial_update)',
            'Automatically maps to urls using Routers',
            'Provides more functionality with less code'
        ]
    
        return Response({'message':'hello','a_viewset':a_viewset})
    
    def create(self,request):
        serializer=self.serializers_class(data=request.data)
        
        if serializer.is_valid():
            name=serializer.validated_data.get('name')

            message=f'hello {name}'

            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    

    def retrive(self,request,pk=None):
        return Response ({'http_metho':'GET'})
    

    def update(sel,request,pk=None):
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})
    
    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})
    

class UserprofileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()