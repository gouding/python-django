from django.shortcuts import render
from people.models import Person 

# ret = Person.objects.get_or_create(name='Wahaha',age=25)
ret = Person.objects.all()

def index (request) :
	content = {}
	content['person'] = ret 
	return render(request,'people/index.html',content)

# Create your views here.
