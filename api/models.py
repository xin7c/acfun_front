# coding=utf-8
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class MOBILE_API(models.Model):
    device = (
        (0, "苹果"),
        (1, "安卓"),
        (2, "其他"),
    )
    api_name = models.CharField(max_length=100, null=True)
    api_version = models.CharField(max_length=100, null=True)
    api_device = models.IntegerField(choices=device)

    def __str__(self):
        return self.api_name
    class Meta:
        verbose_name = '移动端API'
        verbose_name_plural = '移动端API'
        ordering = ['id']  # 按照哪个栏目排序
