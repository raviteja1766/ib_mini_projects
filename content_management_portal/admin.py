from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from content_management_portal.models import *


admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(RoughSolution)
admin.site.register(CleanSolution)
admin.site.register(SolutionApproach)
admin.site.register(PrefilledCode)
admin.site.register(Hint)
admin.site.register(TestCase)
