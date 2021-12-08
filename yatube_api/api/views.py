from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer, FollowSerializer
from .serializers import GroupSerializer, PostSerializer
from posts.models import Post, Group


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get_post(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_queryset(self):
        return self.get_post().comments


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=user__username', '=following__username',)

    def get_queryset(self):
        return self.request.user.user.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
