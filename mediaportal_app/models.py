from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name


def generate_filename(instance, filename):
	filaneme = instance.slug + '.jpg'
	return "{0}/{1}".format(instance, filename)


class Article(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120)
	image = models.ImageField(upload_to=generate_filename)
	content = models.TextField()
	likes = models.PositiveIntegerField(default=0)
	dislikes = models.PositiveIntegerField(default=0)

	def __str__(self):
		return "{0} ({1})".format(str(self.id), self.category)
