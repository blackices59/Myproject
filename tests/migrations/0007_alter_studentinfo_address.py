# Generated by Django 3.2.5 on 2022-05-30 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_alter_studentinfo_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='address',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='文件地址'),
        ),
    ]
