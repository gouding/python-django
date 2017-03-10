from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(u'标题',max_length=256)
	sub_title = models.CharField(u'子标题',max_length=256,null=True)
	content = models.TextField(u'内容')
	author = models.CharField(u'作者',max_length=256,default='Denzel')
	# tag = models.IntegerField(u'博客ID')
	# tag = models.CharField(u'博客ID',max_length=256,default=str(time.time()).split('.')[0])
	tag = models.AutoField(primary_key=True)

	pub_date = models.DateTimeField(u'发布时间',auto_now_add=True,editable=True)
	update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)

	def __str__(self):
		return self.title



# 文章 类

# 字段 
'''
title
sub_title
content
insert_date
author
'''
