from django.db import models


# Create your models here.
# from django.db import models
#
# # Create your models here.
#
# from django.db import models
#
#
# # Create your models here.
#
class Sdept(models.Model):
    sdeptId = models.CharField(verbose_name="学院ID", max_length=20, primary_key=True)
    sdeptName = models.CharField(verbose_name="学院名", max_length=20)

    def __str__(self):
        return self.sdeptName


class Student(models.Model):
    sno = models.CharField(verbose_name="学号", max_length=32, primary_key=True)
    sname = models.CharField(verbose_name="姓名", max_length=32)
    gender_choices = (
        (1, "男"),
        (2, "女"),
    )
    sgender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)
    sage = models.SmallIntegerField(verbose_name="年龄", default=18)
    depart = models.ForeignKey(verbose_name="部门", to="Sdept", on_delete=models.CASCADE)

    def __str__(self):
        return self.sname


class Course(models.Model):
    cno = models.CharField(verbose_name="课程号", max_length=32, primary_key=True)
    cname = models.CharField(verbose_name="课程名", max_length=32)
    # cpno = models.CharField(verbose_name="先修课程号", max_length=32, null=True)
    # cpno 与cno 互为外键
    # 课程号为主键，先修课程号为外键
    cpno = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, verbose_name="先修课",
                             default=None)
    ccredit = models.CharField(verbose_name="学分", max_length=32)

    def __str__(self):
        return self.cname


class Sc(models.Model):
    # sno = models.CharField(verbose_name="学号", max_length=32)
    # cno = models.CharField(verbose_name="课程号", max_length=32)

    # sno 是 Student 的外键
    sno = models.ForeignKey(to="Student", to_field="sno", on_delete=models.CASCADE)
    cno = models.ForeignKey(to="Course", to_field="cno", on_delete=models.CASCADE)
    grade = models.SmallIntegerField(verbose_name="成绩")


class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=12)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username
