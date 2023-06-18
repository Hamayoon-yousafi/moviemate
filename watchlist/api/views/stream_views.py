from ...models import StreamPlatform
from ..serializers import StreamPlatFormSerializer
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView


class StreamPlatFormAV(APIView):
    
    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatFormSerializer(platforms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class StreamPlatFormDetailAV(APIView):
    
    def get(self, request, pk):
        platform = StreamPlatform.objects.get(id=pk)
        serializer = StreamPlatFormSerializer(platform, many=False, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(id=pk)
        serializer = StreamPlatFormSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(id=pk)
        platform.delete()
        return Response(status=204)