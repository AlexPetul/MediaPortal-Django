from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView, View
from django.views.generic.detail import DetailView
from mediaportal_app.models import Category, Article, Comments
from mediaportal_app.forms import CommentCreationForm
from django.http import JsonResponse


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
		context['article_comments'] = self.get_object().comments.all().order_by('-timestamp')
		context['form'] = CommentCreationForm()
		return context


class CreateCommentView(View):
	template_name = 'article_detail.html'

	def post(self, request, *args, **kwargs):
		article_id = request.POST.get('article_id')
		comment = request.POST.get('comment')
		comment = Comments(author=request.user, comment=comment)
		comment.save()
		new_post_template = render(request, 'new_post.html', {'comment': comment})
		article = Article.objects.get(id=article_id)
		article.comments.add(comment)
		article.save()
		return HttpResponse(new_post_template)
