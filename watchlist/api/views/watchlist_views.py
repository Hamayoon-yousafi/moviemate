from ...models import WatchList
from ..serializers import WatchListSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from ..permissions import *


# class based views using APIView
class WatchListAV(APIView):
    permission_classes = [IsAdminOrReadonly]

    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
        

# individual watch class view
class WatchDetailsAV(APIView):
    permission_classes = [IsAdminOrReadonly]

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'The movie was not found.'}, status=404)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'The watchlist was not found.'}, status=404)

        serializer = WatchListSerializer(movie, data=request.data) # if the instance to be updated is not passed (movie), a new instance will be created instead of the existing instance being updated
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
        
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(id=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'The WatchList was not found.'}, status=404)
        
        movie.delete()
        return Response(status=204)
    








# function based views
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         else:
#             return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     try:
#         movie = Movie.objects.get(id=pk)
#     except Movie.DoesNotExist:
#         return Response({'Error': 'The movie was not found.'}, status=404)
    
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data) # if the instance to be updated is not passed (movie), a new instance will be created instead of the existing instance being updated
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)

#     if request.method == 'DELETE':
#         movie.delete()
#         return Response(status=204)