from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import stream_views, watchlist_views, review_views


# creating router for StreamPlatform ViewSet class
router = DefaultRouter()
router.register('stream', stream_views.StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', watchlist_views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', watchlist_views.WatchDetailsAV.as_view(), name='movie-details'),

    # routes for stream using APIView
    # path('streams/', stream_views.StreamPlatFormAV.as_view(), name='stream'),
    # path('streams/<int:pk>/', stream_views.StreamPlatFormDetailAV.as_view(), name='stream-details'),

    # routes for stream using ViewSet class
    path('', include(router.urls)),

    path('watchlist/<int:watchlist_id>/review-create/', review_views.ReviewCreate.as_view(), name='review-create'),
    path('watchlist/<int:watchlist_id>/reviews/', review_views.ReviewList.as_view(), name='review-list'),
    path('watchlist/reviews/<int:pk>/', review_views.ReviewDetail.as_view(), name='review-detail'),
]