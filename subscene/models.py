from django.db import models


from PIL import Image
# Create your models here.

# CATEGORY_CHOICES = (
#     ('HR', 'HackerRank'),
#     ('F', 'Freelancing'),
#     ('DS', 'DataScience')
# )


class Post(models.Model):

	title=models.CharField(max_length=30)
	# image = models.ImageField(default='default.jpg', upload_to='post_pic')
	# document = models.FileField(upload_to='documents/', default ='null')
	# Category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
	image = models.ImageField(default='default.jpg', upload_to='gallery')
	
	document = models.FileField(upload_to='documents/', default ='null') 

	def __str__(self):
		return self.title
	def save(self):
		super().save()
		# img = Image.open(self.image.path)
		img = Image.open(self.image.path)
		if img.height > 300 or img.width > 300:
			output_size = (400, 400)
			img.thumbnail(output_size)
			img.save(self.image.path)