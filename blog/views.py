from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers
from .models import Post

@api_view(['GET'])
def posts_list(requset):
    queryset = Post.objects.all()
    serializer = PostSerializers(queryset, many=True)
    return Response(serializer.data)
    


