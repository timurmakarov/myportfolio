from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .models import Project

def index(request):
	latest_projects_list = Project.objects.order_by('-pub_date')[:3]
	return render(request, 'projects/index.html', {'latest_projects_list': latest_projects_list })

def all(request):
	all_projects_list = Project.objects.order_by('-pub_date')[:15]
	return render(request, 'projects/all.html', {'all_projects_list': all_projects_list })		

def about(request, project_id):	
	try:
		a = Project.objects.get( id = project_id )
	except:
		raise Http404('Проект не найден!')

	return render(request, 'projects/about.html', {'project': a})



