from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_home_page,name="user-home-page"),
    path('create-voter',views.register_voter,name="create-voter"),
#     path('create-user',views.UserCreateView.as_view(),name="create-user"),   
#     path('create-voter',views.VoterCreateView.as_view(),name="create-voter"),
# #    path('create-voter',views.register_user2,name="create-voter"),

    path('create-candidate',views.register_candidate,name="create-candidate"),
    path('create-invigilater',views.register_invigilater,name="create-invigilater"),
]
