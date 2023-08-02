from ...models import Review, WatchList
from ..serializers import ReviewSerializer
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from ..permissions import IsAdminOrReadonly, IsReviewUserOrReadonly
from ..utils import calculate_number_of_ratings_and_average_ratings
from ..throttling import ReviewCreateThrottle
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class UserReview(generics.ListAPIView):
    serializer_class = ReviewSerializer

    # for finding specific user reviews 
    # def get_queryset(self):
    #     review_user = self.kwargs['review_user']
    #     return Review.objects.filter(review_user__username=review_user)
    
    def get_queryset(self):
        return Review.objects.filter(review_user__username=self.request.query_params['username'])

class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [ReviewCreateThrottle]

    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        watchlist_id = self.kwargs['watchlist_id']
        watchlist = WatchList.objects.get(pk=watchlist_id)

        review_queryset = self.get_queryset().filter(watchlist=watchlist, review_user=self.request.user)
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this watchlist.')
        
        calculate_number_of_ratings_and_average_ratings(watchlist, serializer)

        serializer.save(watchlist=watchlist, review_user=self.request.user)


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'review-list'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['review_user__username', 'active']
    search_fields = ['description', 'active']
    ordering_fields = ['rating', 'created']

    def get_queryset(self):
        watchlist_id = self.kwargs['watchlist_id']
        return Review.objects.filter(watchlist=watchlist_id)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadonly]




# using generics.GenericAPIView class with mixins CRUD classes
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class ReviewDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)