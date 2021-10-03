from django.db import models

class Meal (models.Model):
    meal_id=models.IntegerField
    mealname=models.CharField(max_length=100)
    mealdescription=models.CharField(max_length=255)
    mealtype=models.CharField(max_length=50)
    mealprice=models.FloatField()

    def __str__(self):
        return self.mealname

class Drink (models.Model):
    drink_id=models.IntegerField
    drinkname=models.CharField(max_length=100)
    drinkdescription=models.CharField(max_length=255)
    drinktype=models.CharField(max_length=50)
    drinkprice=models.FloatField()

    def __str__(self):
        return self.drinkname

        


