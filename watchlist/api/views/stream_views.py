from ...models import StreamPlatform
from ..serializers import StreamPlatFormSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
from rest_framework import viewsets


# ---class based views using ModelViewSet
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatFormSerializer



# ---class based views using Viewsets
# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatFormSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         stream = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatFormSerializer(stream, context={'request': request})
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = StreamPlatFormSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    
#     def destroy(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         stream = get_object_or_404(queryset, pk=pk)
#         stream.delete()
#         return Response(status=204)


# ---class based views using APIView
# class StreamPlatFormAV(APIView):
    
#     def get(self, request):
#         platforms = StreamPlatform.objects.all()
#         serializer = StreamPlatFormSerializer(platforms, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StreamPlatFormSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# class StreamPlatFormDetailAV(APIView):
    
#     def get(self, request, pk):
#         platform = StreamPlatform.objects.get(id=pk)
#         serializer = StreamPlatFormSerializer(platform, many=False, context={'request': request})
#         return Response(serializer.data)

#     def put(self, request, pk):
#         platform = StreamPlatform.objects.get(id=pk)
#         serializer = StreamPlatFormSerializer(platform, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)
    
#     def delete(self, request, pk):
#         platform = StreamPlatform.objects.get(id=pk)
#         platform.delete()
#         return Response(status=204)