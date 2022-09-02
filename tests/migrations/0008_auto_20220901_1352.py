# Generated by Django 3.2.5 on 2022-09-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0007_auto_20220901_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo1',
            name='brand',
            field=models.CharField(choices=[('红标', '红标'), ('银标', '银标'), ('光标', '光标'), ('宝骏', '宝骏'), ('新宝骏', '新宝骏')], max_length=50, verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='carmodel',
            field=models.CharField(choices=[('730S', '730S'), ('310S', '310S'), ('730M', '730M'), ('220M', '220M')], max_length=50, verbose_name='车型'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='emissionRegulations',
            field=models.CharField(choices=[('国五', '国五'), ('国六A', '国六A'), ('国六B 一类', '国六B 一类'), ('国六B 二类', '国六B 二类')], max_length=50, verbose_name='排放法规'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='engine',
            field=models.CharField(choices=[('N15A', 'N15A'), ('N15T', 'N15T'), ('S15T', 'S15T'), ('LJ2.0T', 'LJ2.0T')], max_length=50, verbose_name='发动机类型'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='gearbox',
            field=models.CharField(choices=[('MT', 'MT'), ('CVT', 'CVT'), ('GF6', 'GF6'), ('混动', '混动')], max_length=50, verbose_name='变速箱类型或混动'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='platform',
            field=models.CharField(choices=[('CN100平台', 'CN100平台'), ('CN180平台', 'CN180平台'), ('CN200平台', 'CN200平台'), ('CN300平台', 'CN300平台'), ('N平台', 'N平台'), ('950平台', '950平台')], max_length=50, verbose_name='车型平台'),
        ),
    ]