from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Products
from .serializers import ProductsSerializer

# Create your views here.

# function to fetch data from json and save in the database.
def fetch_json(request):
    print('WORKING')
    # Fetch data from the external API
    url = 'https://s3.amazonaws.com/open-to-cors/assignment.json'
    response = requests.get(url)
    data = response.json()
    data = data["products"]

    data_list = [value for value in data.values()]

    for item_data in data_list:

        if not Products.objects.filter(subcategory = item_data['subcategory'], title = item_data['title'], price = item_data['price'], popularity = item_data['popularity']).exists():
            serializer = ProductsSerializer(data = item_data)

            if serializer.is_valid():
                serializer.save()
            else :
                print(serializer.errors)

    return HttpResponse("Data saved successfully!!!")


# Locally hosted API to be used to fetch the JSON data in frontend.
@api_view(['GET', ])
def json_data(request) :
    if request.method == 'GET' :
        tasks = Products.objects.all()
        serialized = ProductsSerializer(tasks, many = True)
        # sort the data based on popularity in descending order.
        sorted_data = sorted(serialized.data, key=lambda x: x.get('popularity', 0), reverse=True)
        return Response(sorted_data)


# function to display json data to users.
def show_json_data(request) :
    return render(request, 'load_json_data.html')
