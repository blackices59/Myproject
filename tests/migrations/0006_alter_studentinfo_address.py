# Generated by Django 3.2.5 on 2022-05-30 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0005_studentinfo_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinfo',
            name='address',
            field=models.FileField(default='0', upload_to='tests/uploads/', verbose_name='文件地址'),
        ),
    ]