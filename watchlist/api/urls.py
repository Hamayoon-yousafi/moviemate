from django.urls import path
from .views import stream_views, watchlist_views, review_views

urlpatterns = [
    path('list/', watchlist_views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', watchlist_views.WatchDetailsAV.as_view(), name='movie-details'),

    path('streams/', stream_views.StreamPlatFormAV.as_view(), name='stream'),
    path('streams/<int:pk>/', stream_views.StreamPlatFormDetailAV.as_view(), name='stream-details'),

    path('stream/<int:pk>/review/', review_views.ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>/', review_views.ReviewDetail.as_view(), name='review-detail'),
]