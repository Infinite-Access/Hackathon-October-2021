from rest_framework import serializers

from webapp.models import Drink, Meal


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('mealname', 'mealdescription', 'mealtype', 'mealprice')



class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('drinkname', 'drinkdescription', 'drinktype', 'drinkprice')
