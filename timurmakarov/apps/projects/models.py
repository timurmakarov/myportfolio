from django.db import models
from mdeditor.fields import MDTextField

class Project(models.Model):
	project_client = models.CharField('Название компании', max_length = 48)
	project_title = models.CharField('Название проекта', max_length = 36)
	project_type = models.CharField('Тип проекта', max_length = 36)
	project_description = models.TextField('Описание проекта')
	project_body = models.TextField('Тело проекта')
	project_cover = models.ImageField('Обложка проекта', upload_to='upload')
	pub_date = models.DateTimeField('Дата публикации')
	content = MDTextField()

	def __str__(self):
		return self.project_title

	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'

class Snippet(models.Model):
	title = models.CharField(max_length = 120)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.title

	def body_preview(self):
		return self.body[:50]