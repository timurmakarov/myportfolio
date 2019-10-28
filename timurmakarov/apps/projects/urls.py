from django.urls import path

from . import views

app_name = 'projects'
urlpatterns = [
	path('', views.index, name = 'index'),
	path('all/', views.all, name = 'all'),
	path('<int:project_id>/', views.about, name = 'about'),
]


