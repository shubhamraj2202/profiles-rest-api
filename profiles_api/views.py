from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers


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
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
