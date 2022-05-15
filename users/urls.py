from django.urls import path
from .views import *

urlpatterns = [
    path('signup/bloger/', BlogerSignUpView.as_view()),
    path('signup/reader/', ReaderSignUpView.as_view()),
    path('login/', CustomAuthTokenView.as_view()),


]
