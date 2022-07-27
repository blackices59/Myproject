# Generated by Django 3.2.5 on 2022-07-26 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0017_alter_platformmodelcode_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='majorplatform',
            name='platform',
            field=models.ForeignKey(limit_choices_to={'pid_id': '0'}, on_delete=django.db.models.deletion.CASCADE, to='webtest.platformmodelcode', to_field='data', unique=True, verbose_name='平台'),
        ),
    ]