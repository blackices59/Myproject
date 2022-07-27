# Generated by Django 3.2.5 on 2022-07-26 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0021_alter_platformmodelcode_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='platformmodelcode',
            name='pid',
            field=models.ForeignKey(blank=True, default=99999, on_delete=django.db.models.deletion.CASCADE, to='webtest.platformmodelcode', verbose_name='自关联标识'),
        ),
    ]