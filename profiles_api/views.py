from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.settings import api_settings

from profiles_api import serializers, models, permissions


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
    serializer_class = serializers.NameSerializer

    def list(self, request):
        names_viewset = [
            'David',
            'Tyler',
            'Rose',
            'Georgia'
        ]

        return Response({'names' : names_viewset})
    

    def create(self, request):
        """create a new name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!!!!'
            return Response({'message' : message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, pk=None):
        """getting an object by its ID"""
        return Response({'HTTP method' : 'GET'})
    

    def update(self, request, pk=None):
        """updating an object"""
        return Response({'HTTP method' : 'PUT'})


    def partial_update(self, request, pk=None):
        """update Partially an object"""
        return Response({'HTTP method' : 'PATCH'})
    

    def destroy(self, request, pk=None):
        """Destroying an object"""
        return Response({'HTTP method' : 'DELETE'})
    

class UserProfileViewSet(viewsets.ModelViewSet):
    """user profile viewset"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """for user login"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    

class ProfileFeedItemViewSet(viewsets.ModelViewSet):
    """user profile viewset"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    
    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)

