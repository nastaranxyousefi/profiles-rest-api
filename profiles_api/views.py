from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class NameApiView(APIView):
    """Name api view"""
    serializer_class = serializers.NameSerializer

    def get(self, request, format=None):
        """Returns a list of names"""
        names = [
            {
                'name 1' : 'Jhon',
                'name 2' : 'Sara',
                'name 3' : 'Taylor'
            }
        ]

        return Response({'names' : names})
    
    def post(self, request):
        """creates a name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk=None):
        """updating an object"""
        return Response({'method' : 'put'})
    
    def patch(self, request, pk=None):
        """updating an object"""
        return Response({'method' : 'patch'})
    
    def delete(self, request, pk=None):
        """updating an object"""
        return Response({'method' : 'delete'})
    

class NameViewSet(viewsets.ViewSet):
    """Test API viewset"""

    def list(self, request):
        names_viewset = [
            'David',
            'Tyler',
            'Rose',
            'Georgia'
        ]

        return Response({'names' : names_viewset})
    