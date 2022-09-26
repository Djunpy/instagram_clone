from django.urls import path

from . import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('favorite-posts/', views.ProfileView.as_view(), name='favorite-posts'),
]