from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('services', views.services, name="services"),
    path('store', views.store, name="store"),
    path('blog', views.blog, name="blog"),
    path('contacts', views.contacts, name="contacts"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)