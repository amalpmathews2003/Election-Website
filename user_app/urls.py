from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_home_page,name="user-home-page"),
    path('create-voter',views.VoterCreateView.as_view(),name="create-voter"),
    path('create-candidate',views.CandidateCreateView.as_view(),
        name="create-candidate"),
    path('create-invigilater',views.InvigilaterCreateView.as_view(),
        name="create-invigilater"),
]
