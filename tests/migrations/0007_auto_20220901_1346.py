# Generated by Django 3.2.5 on 2022-09-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0006_rename_projectinfo_projectinfo1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectinfo1',
            name='brand',
            field=models.SmallIntegerField(choices=[('红标', '红标'), ('银标', '银标'), ('光标', '光标'), ('宝骏', '宝骏'), ('新宝骏', '新宝骏')], verbose_name='品牌'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='carmodel',
            field=models.SmallIntegerField(choices=[('730S', '730S'), ('310S', '310S'), ('730M', '730M'), ('220M', '220M')], verbose_name='车型'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='emissionRegulations',
            field=models.SmallIntegerField(choices=[('国五', '国五'), ('国六A', '国六A'), ('国六B 一类', '国六B 一类'), ('国六B 二类', '国六B 二类')], verbose_name='排放法规'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='engine',
            field=models.SmallIntegerField(choices=[('N15A', 'N15A'), ('N15T', 'N15T'), ('S15T', 'S15T'), ('LJ2.0T', 'LJ2.0T')], verbose_name='发动机类型'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='gearbox',
            field=models.SmallIntegerField(choices=[('MT', 'MT'), ('CVT', 'CVT'), ('GF6', 'GF6'), ('混动', '混动')], verbose_name='变速箱类型或混动'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='platform',
            field=models.SmallIntegerField(choices=[('CN100平台', 'CN100平台'), ('CN180平台', 'CN180平台'), ('CN200平台', 'CN200平台'), ('CN300平台', 'CN300平台'), ('N平台', 'N平台'), ('950平台', '950平台')], verbose_name='车型平台'),
        ),
        migrations.AlterField(
            model_name='projectinfo1',
            name='projectProcess',
            field=models.SmallIntegerField(choices=[('台架数据锁定', '台架数据锁定'), ('VBC和排温检查标定', 'VBC和排温检查标定'), ('排放标定和GPF标定', '排放标定和GPF标定'), ('OBD标定', 'OBD标定'), ('数据固化', '数据固化')], verbose_name='项目进度'),
        ),
    ]
