# Generated by Django 3.2.5 on 2022-06-01 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0018_auto_20220531_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]