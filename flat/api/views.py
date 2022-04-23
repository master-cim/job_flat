from asyncio.windows_events import NULL
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters
from rest_framework import mixins

from posts.models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """
    Публикации могут создавать и редактировать
    только авторизованные пользователи
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    pagination_class = LimitOffsetPagination
    ordering_fields = '__all__'
    ordering = ('pub_date',)

    @action(detail=True, methods=['patch'])
    def highlight(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(post.highlighted)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Отбираем только нужные комментарии к посту"""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return Comment.objects.filter(post=post, parent_comm__isnull=True)

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=get_object_or_404(Post, id=self.kwargs.get('post_id'))
        )


class CommentTreeViewSet(viewsets.ModelViewSet):
    """Отображаем дерево комментариев"""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def get_queryset(self):
        com = get_object_or_404(Comment, id=self.kwargs.get('comm_id'))
        return Comment.objects.filter(parent_comm=com)
