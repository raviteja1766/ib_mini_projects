from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from smart_food_management.models import *


admin.site.register(User, UserAdmin)