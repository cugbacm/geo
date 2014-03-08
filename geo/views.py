from django.shortcuts import render
from django.template import Context, loader
from geo.models import Teacher
from django.http import HttpResponse
# Create your views here.
def teacherList(request):
	teacherList = Teacher.objects.order_by('-name')[:5]
	context = {'teacherList' : teacherList}
	return render(request, 'geo/teacherList.html', context)
	#return HttpResponse("hello")

def teacher(request, teacher_id):
	#return render(request, 'geo/teacher.html', {})
	teacher = Teacher.objects.get(id=teacher_id)
	teacherList = Teacher.objects.all()
	#return HttpResponse(teacher.name)
	return render(request, 'geo/teacher.html', {'teacher':teacher, 'teacherList':teacherList})

def index(request):
	return render(request, 'geo/index.html',{})

def chengguojianjie(request):
	return render(request, 'geo/chengguojianjie.html', {})

def zywcr(request):
	return render(request, 'geo/zywcr.html', {})