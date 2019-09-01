from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from . import serializers, models, permissions


class HelloAPIView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of API View features"""
        api_view = [
            "Uses method (post, get, put, patch, delete)",
            "Similar to traditional django view",
            "Gives control over logic",
            "Is mapped to URLs",
        ]

        return Response({
                "Message": "Hello",
                "Api": api_view
            })

    def post(self, request):
        """Create Hello Message with Name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({
                "message": message
            })
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"message": "PUT"})

    def patch(self, request, pk=None):
        """Handle partial updating an object"""
        return Response({"message": "PATCH"})

    def delete(self, request, pk=None):
        """Handle deleting an object"""
        return Response({"message": "DELETE"})


class HelloViewSet(viewsets.ViewSet):
    """Test API View Set"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return Hello Message"""
        a_view_set = [
            'uses_action ,(List, Create, Retrieve, Update, Partial Update)',
            'Automatically maps to URL using Routers',
            'Provides more functionality with Less Code',
        ]
        return Response({
            "message": "Hello View Set",
            "view_set": a_view_set,
        })

    def create(self, request):
        """Create a Hello Message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle Creating and Updating Profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginAPI(ObtainAuthToken):
    """Handle User Authentication Token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles Creating, Reading & Updating of Profile Feed Item """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus, IsAuthenticated,)

    def perform_create(self, serializer):
        """
        Sets the Feed Item to Logged in User,
        Called during HTTP POST
        """
        serializer.save(user_profile=self.request.user)