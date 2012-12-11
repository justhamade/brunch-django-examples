from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'todos': reverse('todo-list', request=request),
    })


class TodoList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = Todo
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = Todo
    serializer_class = TodoSerializer
