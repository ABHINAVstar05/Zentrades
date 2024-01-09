from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Products
from .serializers import ProductsSerializer

# Create your views here.


@api_view(['GET', ])
def fetch_json(request):
    # Fetch data from the external API
    url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'
    response = requests.get(url)
    data = response.json()
    data = data["products"]

    data_list = [value for value in data.values()]

    for item_data in data_list:
        serializer = ProductsSerializer(data = item_data)
        if serializer.is_valid():
            serializer.save()
        else :
            print(serializer.errors)

    return Response({"message": "Data saved successfully"}, status=status.HTTP_201_CREATED)
