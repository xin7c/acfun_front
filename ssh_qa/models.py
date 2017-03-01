# coding=utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models


@python_2_unicode_compatible
class Frontdb(models.Model):
    projectName = models.CharField(max_length=200)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.projectName

    class Meta:
        verbose_name = "前端项目"
        verbose_name_plural = "前端项目"
        ordering = ['id']  # 按照哪个栏目排序