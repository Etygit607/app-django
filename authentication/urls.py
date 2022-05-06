from django.urls import path
from .views import Register, sign_in, sign_out


urlpatterns = [
    path('', Register.as_view(), name="sign_up"),
    path('login/', sign_in , name="sign_in"),
    path('logout/', sign_out , name="sign_out"),
]