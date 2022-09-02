# Generated by Django 3.2.5 on 2022-08-31 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=10, verbose_name='商标')),
            ],
            options={
                'verbose_name': '商标',
                'verbose_name_plural': '商标',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.CharField(max_length=10, verbose_name='发动机型号')),
            ],
            options={
                'verbose_name': '发动机型号',
                'verbose_name_plural': '发动机型号',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=10, verbose_name='车型平台')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.brand', verbose_name='关联的商标')),
            ],
            options={
                'verbose_name': '车型平台',
                'verbose_name_plural': '车型平台',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=10, verbose_name='车型代码')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.platform', verbose_name='关联的车型平台')),
            ],
            options={
                'verbose_name': '车型代码',
                'verbose_name_plural': '车型代码',
            },
        ),
        migrations.CreateModel(
            name='Gearbox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gearbox', models.CharField(max_length=10, verbose_name='变速箱型号')),
                ('engine', models.ManyToManyField(to='tests.Engine')),
            ],
            options={
                'verbose_name': '变速箱型号',
                'verbose_name_plural': '变速箱型号',
            },
        ),
        migrations.AddField(
            model_name='engine',
            name='model',
            field=models.ManyToManyField(to='tests.Model'),
        ),
        migrations.CreateModel(
            name='Emissionstandard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emissionstandard', models.CharField(max_length=10, verbose_name='排放法规')),
                ('gearbox', models.ManyToManyField(to='tests.Gearbox')),
            ],
            options={
                'verbose_name': '排放法规',
                'verbose_name_plural': '排放法规',
            },
        ),
    ]
