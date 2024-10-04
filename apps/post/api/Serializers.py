from rest_framework.serializers import ModelSerializer
from apps.post.models import Post

class PostSerializers(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        #fields = ['title','description','order','created_at']