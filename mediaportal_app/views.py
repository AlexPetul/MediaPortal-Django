from django.shortcuts import render
from django.views.generic.list import ListView
from mediaportal_app.models import Category


class CategoryListView(ListView):
	model = Category
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryListView, self).get_context_data(*args, **kwargs)
		context['categories'] = self.model.objects.all()
		return context