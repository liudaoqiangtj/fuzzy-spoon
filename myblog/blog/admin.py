from django.contrib import admin
from . import models
# Register your models here.
#当前应用的后台管理系统配置
from . import models
class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','content','pub_time')
	list_filter = ('pub_time',)
admin.site.register(models.Article,ArticleAdmin)