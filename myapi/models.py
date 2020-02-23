from django.db import models
from django.contrib.auth.models import User
from PIL import Image

from django.urls import reverse
# Create your models here.



class Post(models.Model):

	title=models.CharField(max_length=30)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpeg', upload_to='gallery')
	
	document = models.FileField(upload_to='documents/', default ='null') 

	def __str__(self):
		return self.title
	def get_absolute_url(self):

		return reverse('detail', args=[self.id])



	
