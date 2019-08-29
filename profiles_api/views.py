from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API view"""

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