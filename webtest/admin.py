from django.contrib import admin
from .models import MajorPlatform, SubProjects, FunctionModules, AnalyticsData

admin.site.register(MajorPlatform)
admin.site.register(SubProjects)
admin.site.register(FunctionModules)
admin.site.register(AnalyticsData)
