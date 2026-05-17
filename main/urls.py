from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('excursion/', views.create_excursion, name="create_excursion_index"),
    path('beach/', views.create_beach, name="create_beach_index"),
    path('ski/', views.create_ski, name="create_ski_index"),
    path('my_tour/', views.my_tour, name="my_tour_index"),
    path('ski_history/', views.ski_history, name="ski_history_index"),
    # Авторизация
    path('login/', auth_views.LoginView.as_view(template_name="main/login/login.html"),name="login"),
    path('logout/', views.logout_views, name="logout"),
    # Регистрация
    path('register/', views.register, name="register")
]