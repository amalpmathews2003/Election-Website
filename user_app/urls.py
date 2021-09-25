from django.urls import path
from . import views
urlpatterns = [
    path('',views.user_home_page,name="user-home-page"),
]
