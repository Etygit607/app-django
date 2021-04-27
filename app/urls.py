from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('services', views.services, name="services"),
    path('store', views.store, name="store"),
    path('blog', views.blog, name="blog"),
    path('contacts', views.contacts, name="contacts"),
]