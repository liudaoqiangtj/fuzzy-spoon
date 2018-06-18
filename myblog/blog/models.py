from django.db import models

# Create your models here.
#数据模型模块，使用ORM框架
class Article(models.Model):
	title = models.CharField(max_length=64,default='Title')
	content = models.TextField(null=True)
	def __str__(self):
		return self.title
	pub_time = models.DateTimeField(auto_now=True)