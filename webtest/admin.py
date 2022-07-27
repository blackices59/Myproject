from django.contrib import admin
from .models import MajorPlatform, SubProjects, FunctionModules, AnalyticsData, PlatformModelCode, ProjectInfo

admin.site.register(MajorPlatform)
admin.site.register(SubProjects)
admin.site.register(FunctionModules)
admin.site.register(AnalyticsData)
admin.site.register(PlatformModelCode)
admin.site.register(ProjectInfo)
