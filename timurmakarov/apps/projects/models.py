from django.db import models

class Project(models.Model):
	project_client = models.CharField('Название компании', max_length = 48)
	project_title = models.CharField('Название проекта', max_length = 36)
	project_type = models.CharField('Тип проекта', max_length = 36)
	project_description = models.TextField('Описание проекта')
	project_body = models.TextField('Тело проекта')
	project_cover = models.ImageField('Обложка проекта', upload_to='upload', height_field=None, width_field=None, max_length=120)
	pub_date = models.DateTimeField('Дата публикации')

	def __str__(self):
		return self.project_title

	class Meta:
		verbose_name = 'Проект'
		verbose_name_plural = 'Проекты'