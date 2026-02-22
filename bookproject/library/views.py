from rest_framework import generics, mixins, status
from rest_framework.response import Response
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer



class AuthorListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class BookDeleteView(
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)