from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.UserRegister.as_view(), name='register'),
	path('login/', views.UserLogin.as_view(), name='login'),
	path('logout/', views.UserLogout.as_view(), name='logout'),
	path('user/', views.UserView.as_view(), name='user'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('cards/create/', views.CardCreateView.as_view(), name='create_card'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
]
