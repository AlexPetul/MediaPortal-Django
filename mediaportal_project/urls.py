from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from mediaportal_app.views import CategoryListView


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', CategoryListView.as_view(), name='categories_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
