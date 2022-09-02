from django.db import models


# # 建立平台-车辆型号-车型代码自关联表
# class PlatformModelCode(models.Model):
#     info = models.CharField(verbose_name='车型特征数据', max_length=100, null=True, blank=True, unique=True)
#     pid = models.ForeignKey('self', blank=True, null=True, verbose_name='自关联标识',
#                             on_delete=models.SET_NULL)
#
#     class Meta:
#         verbose_name = '平台-车辆型号-车型代码自关联表'  # 在admin站点中显示的名称
#         verbose_name_plural = verbose_name  # 显示的复数名称
#
#     def __str__(self):
#         return self.info


# 建立自关联表，自联关系为：车辆商标-车型平台-车型代码-发动机型号-变速箱型号-排放法规
class RelationshipTable(models.Model):
    info = models.CharField(verbose_name='车辆信息', max_length=50, null=True, blank=True)
    relationship = models.ForeignKey('self', verbose_name='关系', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '车辆商标-车型平台-车型代码-发动机型号-变速箱型号-排放法规自关联表'  # 在admin站点中显示的名称
        verbose_name_plural = verbose_name  # 显示的复数名称

    def __str__(self):
        return self.info


class Student(models.Model):
    sex = (
        (1, '男'),
        (2, '女'),
    )
    name = models.CharField(verbose_name='名字', max_length=20)
    sex = models.SmallIntegerField(verbose_name='性别', choices=sex)
    tel = models.CharField(verbose_name='电话', max_length=11)

    class Meta:
        verbose_name = '学生信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 商标
class Brand(models.Model):
    brand = models.CharField(verbose_name='商标', max_length=10)

    class Meta:
        verbose_name = '商标'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.brand


# 车型平台
class Platform(models.Model):
    platform = models.CharField(verbose_name='车型平台', max_length=10)
    brand = models.ForeignKey(Brand, verbose_name='关联的商标', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '车型平台'
        verbose_name_plural = verbose_name

    def __str__(self):
        info = str(self.brand) + '-' + str(self.platform)
        return info


# 车型代码
class Model(models.Model):
    model = models.CharField(verbose_name='车型代码', max_length=10)
    platform = models.ForeignKey(Platform, verbose_name='关联的车型平台', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '车型代码'
        verbose_name_plural = verbose_name

    def __str__(self):
        info = str(self.platform) + '-' + str(self.model)
        return info


# 发动机型号
class Engine(models.Model):
    engine = models.CharField(verbose_name='发动机型号', max_length=10)
    model = models.ManyToManyField(Model)

    class Meta:
        verbose_name = '发动机型号'
        verbose_name_plural = verbose_name

    def __str__(self):
        info = str(self.model) + '-' + str(self.engine)
        return info


# 变速箱型号
class Gearbox(models.Model):
    gearbox = models.CharField(verbose_name='变速箱型号', max_length=10)
    model = models.ManyToManyField(Model)

    class Meta:
        verbose_name = '变速箱型号'
        verbose_name_plural = verbose_name

    def __str__(self):
        info = str(self.model) + '-' + str(self.gearbox)
        return info


# 排放法规
class Emissionstandard(models.Model):
    emissionstandard = models.CharField(verbose_name='排放法规', max_length=10)
    model = models.ManyToManyField(Model)

    class Meta:
        verbose_name = '排放法规'
        verbose_name_plural = verbose_name

    def __str__(self):
        info = str(self.model) + '-' + str(self.emissionstandard)
        return info


class ProjectInfo1(models.Model):
    """项目"""
    brand_choice = (
        ('红标', '红标'),
        ('银标', '银标'),
        ('光标', '光标'),
        ('宝骏', '宝骏'),
        ('新宝骏', '新宝骏'),
    )
    platform_choice = (
        ('CN100平台', 'CN100平台'),
        ('CN180平台', 'CN180平台'),
        ('CN200平台', 'CN200平台'),
        ('CN300平台', 'CN300平台'),
        ('N平台', 'N平台'),
        ('950平台', '950平台'),
    )
    carmodel_choice = (
        ("730S", "730S"),
        ("310S", "310S"),
        ("730M", "730M"),
        ("220M", "220M"),
    )
    engine_choice = (
        ("N15A", "N15A"),
        ("N15T", "N15T"),
        ("S15T", "S15T"),
        ("LJ2.0T", "LJ2.0T"),
    )
    gearbox_choice = (
        ("MT", "MT"),
        ("CVT", "CVT"),
        ("GF6", "GF6"),
        ("混动", "混动"),
    )
    emissionRegulations_choice = (
        ("国五", "国五"),
        ("国六A", "国六A"),
        ("国六B 一类", "国六B 一类"),
        ("国六B 二类", "国六B 二类"),
    )
    projectProcess_choice = (
        ("台架数据锁定", "台架数据锁定"),
        ("VBC和排温检查标定", "VBC和排温检查标定"),
        ("排放标定和GPF标定", "排放标定和GPF标定"),
        ("OBD标定", "OBD标定"),
        ("数据固化", "数据固化"),
    )
    brand = models.CharField(verbose_name='品牌', max_length=50, choices=brand_choice)
    platform = models.CharField(verbose_name='车型平台', max_length=50, choices=platform_choice)
    carmodel = models.CharField(verbose_name="车型", max_length=50, choices=carmodel_choice)
    engine = models.CharField(verbose_name="发动机类型", max_length=50, choices=engine_choice)
    gearbox = models.CharField(verbose_name="变速箱类型或混动", max_length=50, choices=gearbox_choice)
    emissionRegulations = models.CharField(verbose_name="排放法规", max_length=50, choices=emissionRegulations_choice)
    sop_time = models.DateField(verbose_name="SOP时间")
    projectProcess = models.CharField(verbose_name="项目进度", max_length=50, choices=projectProcess_choice)
    # duty_officer = models.ForeignKey(MyUser, verbose_name="项目负责人", on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_time = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        self.allname = str(self.brand)+"-"+str(self.platform)+"-"+str(self.carmodel)+"-"+str(self.engine)+"-"+\
                       str(self.gearbox)+"-"+str(self.emissionRegulations)
        return self.allname
