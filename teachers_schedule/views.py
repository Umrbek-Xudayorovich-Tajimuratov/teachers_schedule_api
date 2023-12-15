import requests
from rest_framework import viewsets
from rest_framework import Response
from .serializers import MyDataSerializer

class MyDataViewSet(viewsets.ViewSet):
    def get(self, request):
        # Fetch data from external API using requests
        response = requests.get("https://api.example.com/data")
        data = response.json()
        # Process and map data to serializer
        serializer = MyDataSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        # Return serialized data
        return Response(serializer.data)
