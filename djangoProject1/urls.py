from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path("", include("improv.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path("admin/", admin.site.urls),

]+ static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
