from django.db import models
from django.contrib.auth.models import User

from PIL import Image
# Create your models here.

# CATEGORY_CHOICES = (
#     ('HR', 'HackerRank'),
#     ('F', 'Freelancing'),
#     ('DS', 'DataScience')
# )


class Post(models.Model):

	title=models.CharField(max_length=30)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='gallery')
	
	document = models.FileField(upload_to='documents/', default ='null') 

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
 #        return reverse('detail', kwargs={'pk': self.pk})

	def save(self):
		super().save()
		# img = Image.open(self.image.path)
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.image.path)