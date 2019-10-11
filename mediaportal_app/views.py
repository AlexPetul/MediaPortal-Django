from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from mediaportal_app.models import Category, Article


class CategoryListView(ListView):
	model = Category
	template_name = 'index.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryListView, self).get_context_data(*args, **kwargs)
		context['categories'] = self.model.objects.all()
		return context


class CategoryDetailView(DetailView):
	model = Category
	template_name = 'category_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		context['categories'] = self.model.objects.all()
		context['category'] = self.get_object()
		context['articles_of_category'] = Article.objects.filter(category__name=self.get_object())
		return context


class ArticleDetailView(DetailView):
	model = Article
	template_name = 'article_detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		context['categories'] = Category.objects.all()
		context['article'] = self.get_object()
		context['article_comments'] = self.get_object().comments.all()
		return context