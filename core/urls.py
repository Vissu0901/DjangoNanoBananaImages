from django.urls import re_path
from . import views

urlpatterns = [
	re_path(r'^register/?$', views.UserRegister.as_view(), name='register'),
	re_path(r'^login/?$', views.UserLogin.as_view(), name='login'),
	re_path(r'^logout/?$', views.UserLogout.as_view(), name='logout'),
	re_path(r'^user/?$', views.UserView.as_view(), name='user'),
    re_path(r'^change-password/?$', views.ChangePasswordView.as_view(), name='change_password'),
    re_path(r'^cards/create/?$', views.CardCreateView.as_view(), name='create_card'),
    re_path(r'^dashboard/?$', views.UserDashboardView.as_view(), name='dashboard'),
]
