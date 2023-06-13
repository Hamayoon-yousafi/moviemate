from django.urls import path
from . import views 

urlpatterns = [
    path('list/', views.MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>', views.MovieDetailsAView.as_view(), name='movie-details'),
]