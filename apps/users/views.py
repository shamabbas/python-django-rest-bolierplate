from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']

    def get_queryset(self):
        pass

    def get_permissions(self):
        pass

    @action(methods=['post'], detail=True)
    def login(self, request, pk=None):
        return Response(status=status.HTTP_202_ACCEPTED)
