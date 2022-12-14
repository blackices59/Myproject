# Generated by Django 3.2.5 on 2022-06-02 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webtest', '0002_auto_20220602_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='functionmodules',
            name='function',
            field=models.CharField(choices=[('售后', '售后数据分析'), ('排放', '排放数据分析'), ('热管理', '热管理数据分析')], max_length=20, unique=True, verbose_name='功能模块'),
        ),
        migrations.AlterField(
            model_name='majorplatform',
            name='create_user',
            field=models.CharField(choices=[('Jiaying Huang', '黄嘉颖')], max_length=20, verbose_name='创建者'),
        ),
        migrations.AlterField(
            model_name='majorplatform',
            name='platform',
            field=models.CharField(choices=[('CN100', 'CN100平台'), ('CN180', 'CN180平台'), ('CN200', 'CN200平台'), ('CN300', 'CN300平台'), ('N', 'N平台'), ('SGMW_950', '950平台')], max_length=20, unique=True, verbose_name='平台'),
        ),
    ]
