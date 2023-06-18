from rest_framework import serializers
from ..models import WatchList, StreamPlatform


# model serializers
class WatchListSerializer(serializers.ModelSerializer):
    platform = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatFormSerializer(serializers.HyperlinkedModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        extra_kwargs = {
            'url': {'view_name': 'stream-details', 'lookup_field': 'pk'} 
            # we can specify what field should be in url so if name is choosen: "url": "http://127.0.0.1:8000/watch/streams/Netflix/". 
            # by default it takes pk as lookup_field so we can clean lookup_field property. but i am leaving it for reference.
        }




# serialization using Serializer class

# def check_if_name_is_valid(value):
#     if len(value) > 45:
#         raise serializers.ValidationError("Name must be less than 45 characters")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[check_if_name_is_valid])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data): # instance is the old object while validated_data is the new object
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['description'] == data['name']:
#             raise serializers.ValidationError("Name and description cannot be the same")
#         return data
    
#     def validate_name(self, value): # value
#         if len(value) < 3:
#             raise serializers.ValidationError('Movie name must be at least more than 3 characters')
#         else:
#             return value