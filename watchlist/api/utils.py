def calculate_number_of_ratings_and_average_ratings(watchlist, review_serializer):
    if watchlist.number_rating == 0:
        watchlist.avg_rating = review_serializer.validated_data['rating']
    else:
        watchlist.avg_rating = (watchlist.avg_rating + review_serializer.validated_data['rating']) / 2
    
    watchlist.number_rating += 1
    watchlist.save()