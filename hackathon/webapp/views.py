from json import dump
from django.http import JsonResponse
from django.shortcuts import render


from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.serializers import DrinkSerializer, MealSerializer
from webapp.models import Drink, Meal



# Create your views here.
class Meals(APIView):

    def get(self, request, *args, **kwargs):
        meals = Meal.objects.all() 
        serialiser = MealSerializer(meals, many=True)
        return Response(serialiser.data)


class Drinks(APIView):
    
    def get(self, request, *args, **kwargs):
        drinks = Drink.objects.all() 
        serializer = DrinkSerializer(drinks, many=True)
        return Response(serializer.data)
