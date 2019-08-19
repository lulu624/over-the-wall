from django.db import models

# Create your models here.

#分类模型
class Category(models.Model):
	name = models.Charfield(max_length=20,version_name="分类名称")
	create_time = models.DateTimeField(auto_now_add=True,version_name="创建时间")
	update_time = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('-create_time')