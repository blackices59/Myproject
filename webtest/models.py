from django.db import models
# from django.utils import timezone


#  层级一，大平台创建
class MajorPlatform(models.Model):
    create_user_choice = (
        ('Jiaying Huang', '黄嘉颖'),
    )
    platform_choice = (
        ('CN100', 'CN100平台'),
        ('CN180', 'CN180平台'),
        ('CN200', 'CN200平台'),
        ('CN300', 'CN300平台'),
        ('N', 'N平台'),
        ('SGMW_950', '950平台'),
    )

    create_user = models.CharField(verbose_name='创建者', max_length=20, choices=create_user_choice)
    platform = models.CharField(verbose_name='平台', max_length=20, unique=True, choices=platform_choice)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        self.show_info = self.platform + ' ' + self.create_user
        return self.show_info


# platform_name = ['CN100', 'CN180', 'CN200', 'CN300', 'N', 'SGMW_950']


# 层级二，子项目
class SubProjects(models.Model):
    create_user_choice = (
        ('Jiaying Huang', '黄嘉颖'),
    )
    model_choice_cn100 = (
        ('CN100_CN100', 'CN100_CN100'),
        ('CN100_CN100V', 'CN100_CN100V'),
        ('CN100_CN101', 'CN100_CN101'),
        ('CN100_CN110P', 'CN100_CN110P'),
        ('CN100_CN110PPS', 'CN100_CN110PPS'),
        ('CN100_CN110V', 'CN100_CN110V'),
        ('CN100_CN112', 'CN100_CN112'),
        ('CN100_CN113', 'CN100_CN113'),
        ('CN100_CN115', 'CN100_CN115'),
        ('CN100_CN120S', 'CN100_CN120S'),
        ('CN100_CN150M', 'CN100_CN150M'),
        ('CN100_CN150V', 'CN100_CN150V'),
    )

    model_choice_cn200 = (
        ('CN200_CN200', 'CN200_CN200'),
    )

    create_user = models.CharField(verbose_name='创建者', max_length=20, choices=create_user_choice)
    platform_info = models.ForeignKey(verbose_name='关联的平台', to=MajorPlatform, to_field='platform',
                                      on_delete=models.CASCADE)
    model = models.CharField(verbose_name='车辆型号', max_length=20, unique=True, choices=model_choice_cn200)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        self.show_info = str(self.platform_info) + ' ' + str(self.model)
        return str(self.show_info)


# model_name = ['CN100_CN100', 'CN100_CN100V', 'CN100_CN101', 'CN100_CN110P', 'CN100_CN110PPS', 'CN100_CN110V',
#               'CN100_CN112', 'CN100_CN113', 'CN100_CN115', 'CN100_CN120S', 'CN100_CN150M', 'CN100_CN150V']


# 层级三，功能块
class FunctionModules(models.Model):
    function_choice = (
        ('售后', '售后数据分析'),
        ('排放', '排放数据分析'),
        ('热管理', '热管理数据分析'),
    )
    model_info = models.ForeignKey(verbose_name='关联的车辆型号', to=SubProjects, to_field='model',
                                   on_delete=models.CASCADE)
    function = models.CharField(verbose_name='功能模块', max_length=20, choices=function_choice)

    def __str__(self):
        return self.function


# 层级四，分析数据存储
class AnalyticsData(models.Model):
    platform_info = models.ForeignKey(verbose_name='所属平台', to=MajorPlatform, to_field='platform',
                                      on_delete=models.CASCADE)
    models_info = models.ForeignKey(verbose_name='所属车型', to=SubProjects, to_field='model', on_delete=models.CASCADE)
    function_info = models.ForeignKey(verbose_name='所属功能模块', to=FunctionModules, on_delete=models.CASCADE)
    data = models.CharField(verbose_name='数据', max_length=256)
    analytics = models.TextField(verbose_name='结果分析')

    def __str__(self):
        self.show_info = str(self.function_info)+' '+str(self.models_info)
        return self.show_info
