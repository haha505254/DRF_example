from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Post
from .serializers import PostSerializer

def index(request):
    
    return render(request,'messageboard/index.html')

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer