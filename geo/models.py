from django.db import models

# Create your models here.
class Teacher(models.Model):
	"""docstring for Teacher"""
	name = models.CharField(max_length = 200)
	sex = models.CharField(max_length = 200)
	come_from = models.CharField(max_length = 200)
	picName = models.CharField(max_length = 200)
	birthday = models.CharField(max_length = 200)
	describe = models.TextField()
	education = models.CharField(max_length = 200)
	workTime = models.DateField("workTime")
	workAge = models.DateField("workAge")
	title = models.CharField(max_length = 200)
	job = models.CharField(max_length = 200)
	colleage = models.CharField(max_length = 200)
	tel = models.CharField(max_length = 200)
	email = models.EmailField(max_length = 200)
	address = models.CharField(max_length = 200)
	postalcode = models.CharField(max_length = 200)
	def  __unicode__(self):
		return self.name

	def save(self):
		super(Teacher, self).save()
		