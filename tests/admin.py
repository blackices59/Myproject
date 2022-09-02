from django.contrib import admin
from . import models
from django.contrib import admin

admin.site.register(models.RelationshipTable)
admin.site.register(models.Student)
admin.site.register(models.Brand)
admin.site.register(models.Platform)
admin.site.register(models.Model)
admin.site.register(models.Engine)
admin.site.register(models.Gearbox)
admin.site.register(models.Emissionstandard)

admin.site.register(models.ProjectInfo1)
