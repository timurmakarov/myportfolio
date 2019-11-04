from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('all/', views.all, name = 'all'),
	path('viewsnprojects/', views.viewsnProjects, name = 'viewsnprojects'),
	path('viewhtml5projects/', views.viewhtml5bannersProjects, name = 'viewhtml5projects'),
	path('<int:project_id>/', views.about, name = 'about'),
]


