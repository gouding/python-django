from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','pub_date','update_time')
	class Media:
		js = (
			'js/kindeditor-4.1.10/kindeditor-all.js',
            'js/kindeditor-4.1.10/lang/zh_CN.js',
            'js/kindeditor-4.1.10/config.js',
		)
admin.site.register(Article,ArticleAdmin)