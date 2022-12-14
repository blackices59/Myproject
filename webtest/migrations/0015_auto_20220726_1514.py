# Generated by Django 3.2.5 on 2022-07-26 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0014_auto_20220726_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorplatform',
            name='platform',
            field=models.ForeignKey(limit_choices_to={'pid_id': '1'}, on_delete=django.db.models.deletion.CASCADE, to='webtest.platformmodelcode', to_field='data', unique=True, verbose_name='平台'),
        ),
        migrations.AlterField(
            model_name='platformmodelcode',
            name='data',
            field=models.CharField(blank=True, default='main', max_length=100, unique=True, verbose_name='车型特征数据'),
        ),
    ]
