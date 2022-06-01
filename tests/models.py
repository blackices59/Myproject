from django.db import models
from django.utils import timezone


class StudentInfo(models.Model):
    sex_choices = (
        ('男', '男'),
        ('女', '女'),
    )

    ethnic_choices = (
        ('汉', '汉'),
        ('壮', '壮'),
    )
    student_id = models.CharField(verbose_name='学号', max_length=15, unique=True)
    name = models.CharField(verbose_name='姓名', db_column='姓名', max_length=10)
    sex = models.CharField(verbose_name='性别', db_column='性别', max_length=5, choices=sex_choices)
    ethnic = models.CharField(verbose_name='民族', db_column='民族', max_length=5, choices=ethnic_choices)
    time = models.DateTimeField(verbose_name='时间', db_column='时间', auto_now=True)
    email = models.EmailField(verbose_name='电子邮箱', db_column='电子邮箱', default='123@qq.com')
    address = models.FileField(verbose_name='文件地址', db_column='文件地址', null=True, blank=True)

    def __str__(self):
        self.allname = self.student_id+" "+self.name
        return self.allname


class StudentGoal(models.Model):
    student = models.ForeignKey(to=StudentInfo, to_field='student_id', on_delete=models.CASCADE, db_index=False)
    chinese = models.CharField(verbose_name='语文', max_length=3)
    math = models.CharField(verbose_name='数学', max_length=3)
    english = models.CharField(verbose_name='英语', max_length=3)

    def __str__(self):
        self.name = str(self.student)
        return self.name


class Test(models.Model):
    pass


platform_name = ['CN100', 'CN180', 'CN200', 'CN300', 'N', 'SGMW_950']
for platform in platform_name:
    Test.add_to_class(platform, models.CharField(verbose_name=platform, db_column=platform, max_length=10,
                                                 null=True, blank=True))
"""
    修改时间：2022.05.30
    修改内容：新增一个类，用于存储上传的售后数据信息，外键关联用户信息。
    
"""


# 售后数据上传存储
class AfterSaleData(models.Model):
    topic = models.CharField(verbose_name='分析数据主题', db_column='分析数据主题', max_length=255)
    note = models.TextField(verbose_name='备注', db_column='备注', default='无')
    file_address = models.FileField(verbose_name='售后数据文件', db_column='售后数据文件', upload_to='tests/uploads/%Y/%m/%d/')
    updata_time = models.DateTimeField(verbose_name='上传时间', db_column='上传时间', default=timezone.now)
    # functionary = models.ForeignKey(verbose_name='上传人', db_column='上传人')

    def __str__(self):
        return self.topic


# 售后数据分析结果存储
class AfterSaleDataAnalyse(models.Model):
    datainfo = models.ForeignKey(to=AfterSaleData, on_delete=models.CASCADE, db_column='售后数据')
    histogram_choices = (
        ('无', '无'),
        ('柱状图', '柱状图'),
    )
    fault_part_histogram_choices = (
        ('无', '无'),
        ('故障部件柱状图', '故障部件柱状图'),
    )
    pie_choices = (
        ('无', '无'),
        ('饼图', '饼图'),
    )
    fault_type_pie_choices = (
        ('无', '无'),
        ('故障种类饼图', '故障种类饼图'),
    )
    fault_part_pie_choices = (
        ('无', '无'),
        ('故障部件饼图', '故障部件饼图'),
    )

    # 柱状图
    histogram = models.CharField(verbose_name='柱状图', db_column='柱状图', max_length=10,
                                 choices=histogram_choices, default='无')
    # 故障部件柱状图
    fault_part_histogram = models.CharField(verbose_name='故障部件柱状图', db_column='故障部件柱状图', max_length=10,
                                            choices=fault_part_histogram_choices, default='无')
    # 饼图
    pie = models.CharField(verbose_name='饼图', db_column='饼图', max_length=10,
                           choices=fault_part_histogram_choices, default='无')
    # 故障类型饼图
    fault_type_pie = models.CharField(verbose_name='故障类型饼图', db_column='故障类型饼图', max_length=10,
                                      choices=fault_type_pie_choices, default='无')
    # 故障部件饼图
    fault_part_pie = models.CharField(verbose_name='故障部件饼图', db_column='故障部件饼图', max_length=10,
                                      choices=fault_part_pie_choices, default='无')

    def __str__(self):
        return str(self.datainfo)


class PictureHistogram(models.Model):
    belong = models.ForeignKey(to=AfterSaleDataAnalyse, verbose_name='所属', on_delete=models.CASCADE)
    cn100 = models.FileField(verbose_name='CN100', db_column='CN100', upload_to='tests/uploads/%Y/%m/%d/CN100/',
                             null=True, blank=True)
    cn180 = models.FileField(verbose_name='CN180', db_column='CN180', upload_to='tests/uploads/%Y/%m/%d/CN180/',
                             null=True, blank=True)
    cn200 = models.FileField(verbose_name='CN200', db_column='CN200', upload_to='tests/uploads/%Y/%m/%d/CN200/',
                             null=True, blank=True)
    cn300 = models.FileField(verbose_name='CN300', db_column='CN300', upload_to='tests/uploads/%Y/%m/%d/CN300/',
                             null=True, blank=True)
    n = models.FileField(verbose_name='N', db_column='N', upload_to='tests/uploads/%Y/%m/%d/N/', null=True, blank=True)
    sgmw_950 = models.FileField(verbose_name='SGMW_950', db_column='SGMW_950',
                                upload_to='tests/uploads/%Y/%m/%d/SGMW_950/', null=True, blank=True)

    def __str__(self):
        return str(self.belong)


class PictureFaultPartHistogram(models.Model):
    belong = models.ForeignKey(to=AfterSaleDataAnalyse, verbose_name='所属', on_delete=models.CASCADE)
    cn100 = models.FileField(verbose_name='CN100', db_column='CN100', upload_to='tests/uploads/%Y/%m/%d/CN100/',
                             null=True, blank=True)
    cn180 = models.FileField(verbose_name='CN180', db_column='CN180', upload_to='tests/uploads/%Y/%m/%d/CN180/',
                             null=True, blank=True)
    cn200 = models.FileField(verbose_name='CN200', db_column='CN200', upload_to='tests/uploads/%Y/%m/%d/CN200/',
                             null=True, blank=True)
    cn300 = models.FileField(verbose_name='CN300', db_column='CN300', upload_to='tests/uploads/%Y/%m/%d/CN300/',
                             null=True, blank=True)
    n = models.FileField(verbose_name='N', db_column='N', upload_to='tests/uploads/%Y/%m/%d/N/', null=True, blank=True)
    sgmw_950 = models.FileField(verbose_name='SGMW_950', db_column='SGMW_950',
                                upload_to='tests/uploads/%Y/%m/%d/SGMW_950/', null=True, blank=True)

    def __str__(self):
        return str(self.belong)
