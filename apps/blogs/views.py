from rest_framework import viewsets

from .models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()

    def get_permissions(self):
        pass
    