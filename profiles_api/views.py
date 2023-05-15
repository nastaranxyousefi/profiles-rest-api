from rest_framework.views import APIView
from rest_framework.response import Response


class NameApiView(APIView):
    """Name api view"""

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