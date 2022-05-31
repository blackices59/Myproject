from django.contrib import admin
from .models import StudentInfo, StudentGoal, AfterSaleData, AfterSaleDataAnalyse

admin.site.register(StudentInfo)
admin.site.register(StudentGoal)
admin.site.register(AfterSaleData)
admin.site.register(AfterSaleDataAnalyse)

