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
		context['carousel_articles'] = Article.objects.all().order_by('-time_added')[:3]
		context['sport_articles'] = Article.objects.filter(category__name='Sport')
		context['hot_articles'] = Article.objects.all().order_by('-time_added')[:6]
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


class DisplayArticlesByCategory(View):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		category = request.GET.get('category')
		articles = Article.objects.filter(category__name=category)
		sub_template = render(request, 'category_results.html', {'articles': articles})
		return HttpResponse(sub_template)


class UserReactionView(View):
	template_name = 'category_detail.html'

	def get(self, request, *args, **kwargs):
		article_id = request.GET.get('article_id')
		article = Article.objects.get(id=article_id)
		query = request.GET.get('query')
		if query == 'like':
			if request.user not in article.users_reactions.all():
				article.likes += 1
				article.users_reactions.add(request.user)
				article.save()
		elif query == 'dislike':
			if request.user not in article.users_reactions.all():
				article.dislikes += 1
				article.users_reactions.add(request.user)
				article.save()
		data = {
			'total_likes': article.likes,
			'total_dislikes': article.dislikes
		}
		return JsonResponse(data)
