# Generated by Django 3.2.5 on 2022-05-27 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=15, unique=True, verbose_name='学号')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('sex', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=5, verbose_name='性别')),
                ('ethnic', models.CharField(choices=[('汉', '汉'), ('壮', '壮')], max_length=5, verbose_name='民族')),
            ],
        ),
        migrations.CreateModel(
            name='StudentGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chinese', models.CharField(max_length=3, verbose_name='语文')),
                ('math', models.CharField(max_length=3, verbose_name='数学')),
                ('english', models.CharField(max_length=3, verbose_name='英语')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.studentinfo', to_field='student_id')),
            ],
        ),
    ]