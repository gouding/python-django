from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Article

# Create your views here.
def index (request):
	content = {};
	ret = Article.objects.all()
	content['res'] = [{'title':'娃哈哈','content':'aaaaa'}]
	content['ret'] = list(ret)
	print(type(content['ret']))
	return render(request,'index.html',content)
	
def home(request):
	ret = Article.objects.all()
	return HttpResponse(ret)