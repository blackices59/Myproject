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
