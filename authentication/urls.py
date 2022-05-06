from django.urls import path
from .views import Register, sign_out


urlpatterns = [
    path('', Register.as_view(), name="sign_up"),
    path('logout/', sign_out , name="sign_out"),
]