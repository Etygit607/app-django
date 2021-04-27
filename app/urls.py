from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('services', views.services, name="Services"),
    path('store', views.store, name="Store"),
    path('blog', views.blog, name="Blog"),
    path('contacts', views.contacts, name="Contacts"),
]