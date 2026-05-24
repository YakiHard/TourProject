from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('excursion/', views.create_excursion, name="create_excursion_index"),
    path('beach/', views.create_beach, name="create_beach_index"),
    path('ski/', views.create_ski, name="create_ski_index"),
    path('my_tour/', views.my_tour, name="my_tour_index"),
    path('ski_history/', views.ski_history, name="ski_history_index"),
    path('null/', views.null, name="null"),
    path('cancel/<int:tour_id>/', views.cancel_tour, name="cancel_tour"),
    path('restart/<int:tour_id>/', views.restart_tour, name="restart_tour"),
    path('delete/<int:tour_id>/', views.delete_tour, name="delete_tour"),
    # Авторизация
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_views, name="logout"),
    # Регистрация
    path('register/', views.register, name="register")
]