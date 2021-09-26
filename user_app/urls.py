from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_home_page,name="user-home-page"),
    path('logout',views.logout_user,name="user-logout"),
    path('login_voter',views.login_user,name="login-voter"),
    path('login_candidate',views.login_user,name="login-candidate"),
    path('login_invigilater',views.login_user,name="login-invigilater"),
    path('create-voter',views.register_voter,name="create-voter"),
    path('create-candidate',views.register_candidate,name="create-candidate"),
    path('create-invigilater',views.register_invigilater,name="create-invigilater"),
    path('redirect',views.redirect,name="redirect"),
    path('satrt_voting',views.start_voting,name="start-voting"),
    path('declare',views.declare_results,name="declare-results")
]
