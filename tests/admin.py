from django.contrib import admin
from .models import StudentInfo, StudentGoal, AfterSaleData, AfterSaleDataAnalyse, PictureHistogram, PictureFaultPartHistogram, Test

admin.site.register(StudentInfo)
admin.site.register(StudentGoal)
admin.site.register(AfterSaleData)
admin.site.register(AfterSaleDataAnalyse)
admin.site.register(PictureHistogram)
admin.site.register(PictureFaultPartHistogram)
admin.site.register(Test)