from django.urls import path
from accounts.views import *


urlpatterns = [
    path('login', LoginView.as_view(), name='sign_in'),
    path('register', RegisterView.as_view(), name='sign_up'),
    path('logout', LogoutView.as_view(), name='sign_out'),
]
