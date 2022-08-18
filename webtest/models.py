from django.db import models
from django.utils import timezone


# 建立平台-车辆型号-车型代码自关联表
class PlatformModelCode(models.Model):
    info = models.CharField(verbose_name='车型特征数据', max_length=100, null=True, blank=True, unique=True)
    pid = models.ForeignKey('self', related_name='beyond', blank=True, null=True, verbose_name='自关联标识',
                            on_delete=models.SET_NULL)

    class Meta:
        verbose_name = '平台-车辆型号-车型代码自关联表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.info


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
    # platform = models.ForeignKey(verbose_name='平台', to=PlatformModelCode, unique=True, to_field='data',
    #                              on_delete=models.CASCADE, limit_choices_to={'pid_id':})
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = '车型平台'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        self.show_info = str(self.platform) + ' ' + self.create_user
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

    class Meta:
        verbose_name = '车型'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

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
                                   on_delete=models.DO_NOTHING)
    function = models.CharField(verbose_name='功能模块', max_length=20, choices=function_choice)

    class Meta:
        verbose_name = '功能模块'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

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

    class Meta:
        verbose_name = '分析数据存储'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        self.show_info = str(self.function_info)+' '+str(self.models_info)
        return self.show_info


class ProjectInfo(models.Model):
    """项目"""
    brand_choice = (
        (1, '红标'),
        (2, '银标'),
        (3, '光标'),
        (4, '宝骏'),
        (5, '新宝骏'),
    )
    platform_choice = (
        (1, 'CN100平台'),
        (2, 'CN180平台'),
        (3, 'CN200平台'),
        (4, 'CN300平台'),
        (5, 'N平台'),
        (6, '950平台'),
    )
    name_chices = (
        (1, "730S"),
        (2, "310S"),
        (3, "730M"),
        (4, "220M"),
    )
    engine_chices = (
        (1, "N15A"),
        (2, "N15T"),
        (3, "S15T"),
        (4, "LJ2.0T"),
    )
    gearbox_chices = (
        (1, "MT"),
        (2, "CVT"),
        (3, "GF6"),
        (4, "混动"),
    )
    EmissionRegulations_chices = (
        (1,"国五"),
        (2,"国六A"),
        (3,"国六B"),
    )
    ProjectProcess_chices = (
        (1, "台架数据锁定"),
        (2, "VBC和排温检查标定"),
        (3, "排放标定和GPF标定"),
        (4, "OBD标定"),
        (5, "数据固化"),
    )
    brand = models.SmallIntegerField(verbose_name='品牌', choices=brand_choice)
    platform = models.SmallIntegerField(verbose_name='车型平台', choices=platform_choice)
    name = models.SmallIntegerField(verbose_name="车型", choices=name_chices)
    engine = models.SmallIntegerField(verbose_name="发动机类型", choices=engine_chices)
    gearbox = models.SmallIntegerField(verbose_name="变速箱类型或混动",choices=gearbox_chices)
    EmissionRegulations = models.SmallIntegerField(verbose_name="排放法规",choices=EmissionRegulations_chices)
    sop_time = models.DateField(verbose_name="SOP时间")
    ProjectProcess = models.SmallIntegerField(verbose_name="项目进度", choices=ProjectProcess_chices)
    # duty_officer = models.ForeignKey(MyUser, verbose_name="项目负责人", on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        verbose_name = '成哥的表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        # self.allname = findname(self.name,self.name_chices)+" "+findname(self.engine,self.engine_chices)+" "+findname(self.gearbox,self.gearbox_chices)
        self.allname = str(self.name) + str(self.engine)
        return self.allname