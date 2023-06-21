from ...models import Review, WatchList
from ..serializers import ReviewSerializer
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        watchlist_id = self.kwargs['watchlist_id']
        watchlist = WatchList.objects.get(pk=watchlist_id)

        review_queryset = self.get_queryset().filter(watchlist=watchlist, review_user=self.request.user)
        if review_queryset.exists():
            raise ValidationError('You have already reviewed this watchlist.')
        
        serializer.save(watchlist=watchlist, review_user=self.request.user)


class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        watchlist_id = self.kwargs['watchlist_id']
        return Review.objects.filter(watchlist=watchlist_id)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


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