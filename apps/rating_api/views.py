from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.manga_api.models import Manga
from apps.rating_api.models import Vote

# Create your views here.
from apps.rating_api.serializers import VoteViewSerializer, VoteUpdateSerializer


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    search_fields = ['manga__slug']
    filter_backends = (filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter)
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    lookup_field = 'manga_id'
    ordering_fields = ['vote_time']
    filterset_fields = ('manga__slug',)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return VoteViewSerializer
        return VoteUpdateSerializer

    def perform_create(self, serializer):
        serializer.save()
        manga = Manga.objects.get(id=self.request.data['manga'])
        votes = manga.vote_set.all()
        overall = 0
        for vote in votes:
            overall += vote.vote_int

        rating = overall / len(votes)
        manga.rating = format(rating, '.2f')
        manga.save()

