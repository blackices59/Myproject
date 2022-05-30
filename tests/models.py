from django.db import models


class StudentInfo(models.Model):
    sex_chices = (
        ('男', '男'),
        ('女', '女'),
    )

    ethnic_chices = (
        ('汉', '汉'),
        ('壮', '壮'),
    )
    student_id = models.CharField(verbose_name='学号', max_length=15, unique=True)
    name = models.CharField(verbose_name='姓名',db_column='姓名', max_length=10)
    sex = models.CharField(verbose_name='性别',db_column='性别', max_length=5, choices=sex_chices)
    ethnic = models.CharField(verbose_name='民族',db_column='民族', max_length=5, choices=ethnic_chices)
    time = models.DateTimeField(verbose_name='时间',db_column='时间', auto_now=True)
    email = models.EmailField(verbose_name='电子邮箱',db_column='电子邮箱', default='123@qq.com')
    address = models.FileField(verbose_name='文件地址',db_column='文件地址', null=True, blank=True)

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