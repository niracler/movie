from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, UpdateModelMixin
from .models import Movie
from .filters import MovieFiliter
from .serializers import MovieSerializer


# Create your views here.

class MoviePagination(PageNumberPagination):
    """用于文章内容分页的类"""
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class MovieViewSet(viewsets.GenericViewSet, ListModelMixin):
    queryset = Movie.objects.all()
    pagination_class = MoviePagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = MovieFiliter
    search_fields = ('mid', 'name')
    ordering_fields = ('mid', 'area_id', 'box_office')

    def get_serializer_class(self):
        return MovieSerializer
