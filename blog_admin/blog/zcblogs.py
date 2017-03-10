from django.shortcuts import render
from blog.models import Article
from datetime import datetime 

def index (request):
	content = {};
	data = Article.objects.all()
	for item in data:
		item.date = datetime.strftime(item.pub_date,'%Y年%m月%d日 %X');
	content['ret'] = data;
	return render(request,'blogs/index.html',content)


def zcdetail(request,blogId):
	blogId = int(blogId)
	content = {}
	blog = Article.objects.get(tag=blogId)
	blog.pub_date = datetime.strftime(blog.pub_date,'%Y年%m月%d日 %X')
	content['blog'] = blog
	print(blog.title)
	return render(request,'blogs/zcdetail.html',content)