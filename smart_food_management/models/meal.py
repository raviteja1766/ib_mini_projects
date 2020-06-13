from django.db import models
from .user import User
from .item import Item
from smart_food_management.constants.enums import MealType, MealSizeType

class Meal(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    meal_type = models.CharField(
        max_length=100, choices=MealType.get_list_of_tuples()
    )
    meal_size = models.CharField(
        max_length=100, choices=MealSizeType.get_list_of_tuples()
    )
    eat_status = models.BooleanField(default=False)
    meal_status = models.BooleanField(default=False)
    items = models.ManyToManyField(Item)
