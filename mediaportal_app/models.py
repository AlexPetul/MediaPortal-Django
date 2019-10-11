from django.db import models
from django.urls import reverse
from django.conf import settings

class Category(models.Model):
	name = models.CharField(max_length=50)
	slug = models.SlugField(max_length=50)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category_detail_view', kwargs={'slug': self.slug})


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
	comments = models.ManyToManyField('Comments')

	def get_absolute_url(self):
		return reverse('article_detail_view', kwargs={'slug': self.slug})

	def __str__(self):
		return "{0} ({1})".format(str(self.id), self.category)


class Comments(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
	comment = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	class Meta:
		verbose_name_plural = "Comments's"

	def __str__(self):
		return str(self.id)