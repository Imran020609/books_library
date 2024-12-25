from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from .filters import BookFilter
from .models import Author, Book
from .serializers import AuthorSerializers, BookSerializers


class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class AuthorCreateAPIView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class AuthorRetrieveAPIView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    lookup_field = 'id'

    def get_object(self):
        try:
            return super().get_object()
        except Author.DoesNotExist:
            raise NotFound("Автор не найден.")


class AuthorUpdateAPIView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())


class AuthorDestroyAPIView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    lookup_field = 'id'

    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise PermissionDenied('Удаление доступно только администраторам.')
        instance.delete()


class BookListAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class BookFilterAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author']


class BookCreateAPIView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class BookRetrieveAPIView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'id'

    def get_object(self):
        try:
            return super().get_object()
        except Book.DoesNotExist:
            raise NotFound("Книга не найдена.")


class BookUpdateAPIView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())


class BookDestroyAPIView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'id'

    def perform_destroy(self, instance):
        if not self.request.user.is_staff:
            raise PermissionDenied("Удаление доступно только администраторам.")
        instance.delete()
