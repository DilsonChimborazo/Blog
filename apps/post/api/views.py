#from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
#from rest_framework.response import Response
#from rest_framework import status
from apps.post.models import Post
from apps.post.api.Serializers import PostSerializers


class postModelViewset(ModelViewSet):
    serializer_class= PostSerializers
    queryset = Post.objects.all()

"""class PostViewSet(ViewSet):
    def list (self, request):
        serializer = PostSerializers(Post.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def retrieve(self, request, pk=int):
        serializer = PostSerializers(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=serializer.data)


    def create (self,request):
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)#validacion de datos correctos
        serializer.save()
        return Response(status=status.HTTP_200_OK, data=serializer.data)"""