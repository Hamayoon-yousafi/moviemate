# from .models import Movie
# from django.http import JsonResponse

# def movie_list(request):
#     movies = Movie.objects.all()
#     return JsonResponse(list(movies.values()), safe=False)

# def movie_details(request, pk):
#     movie = Movie.objects.get(id=pk)
#     data = {'id': movie.id, 'name': movie.name, 'description': movie.description, 'active': movie.active}
#     return JsonResponse(data)