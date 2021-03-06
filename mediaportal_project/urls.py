from django.contrib import admin
from django.contrib.auth.views import LogoutView, PasswordChangeView
from django.urls import path, re_path, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from mediaportal_app.views import (CategoryListView, CategoryDetailView, ArticleDetailView, CreateCommentView, 
	DisplayArticlesByCategory, UserReactionView, RegisterUserView, LoginUserView, UserAccountView, AddArticlesToFavoutitesView,
	SearchView)


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', CategoryListView.as_view(), name='categories_view'),
    re_path(r'^category/(?P<slug>[-\w]+)/$', CategoryDetailView.as_view(), name='category_detail_view'),
    re_path(r'^search/$', SearchView.as_view(), name='search_view'),
    re_path(r'^article/(?P<category_slug>[-\w]+)/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article_detail_view'),
    re_path(r'^add_comment/$', CreateCommentView.as_view(), name='create_comment_view'),
    re_path(r'^add_article_to_favourites/$', AddArticlesToFavoutitesView.as_view(), name='add_article_to_favourites_view'),
    re_path(r'^send_like_dislike/$', UserReactionView.as_view(), name='user_reaction_view'),
    re_path(r'^display_articles_by_category/$', DisplayArticlesByCategory.as_view(), name='display_articles_by_category_view'),
    re_path(r'^sign_up/$', RegisterUserView.as_view(), name='registration_view'),
    re_path(r'^sign_in/$', LoginUserView.as_view(), name='login_view'),
    re_path(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('categories_view')), name='logout_view'),
    re_path(r'^change_password/$', PasswordChangeView.as_view(success_url=reverse_lazy('categories_view')), name='change_password_view'),
    re_path(r'^user/(?P<user>[-\w]+)/$', UserAccountView.as_view(), name='account_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
