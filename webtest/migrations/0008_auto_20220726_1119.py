# Generated by Django 3.2.5 on 2022-07-26 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0007_auto_20220602_1429'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AnalyticsData',
        ),
        migrations.DeleteModel(
            name='FunctionModules',
        ),
        migrations.DeleteModel(
            name='MajorPlatform',
        ),
        migrations.DeleteModel(
            name='SubProjects',
        ),
    ]
