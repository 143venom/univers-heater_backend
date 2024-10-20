from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, APIException
from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer

from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-id')
    serializer_class = BlogSerializer
    lookup_field = 'slug'

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response({'message': 'Blog created successfully', 'data': response.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        try:
            response = super().update(request, *args, **kwargs)
            return Response({'message': 'Blog updated successfully', 'data': response.data}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        blog_id = self.kwargs.get('blog_pk')
        if blog_id:
            return Comment.objects.filter(blog__pk=blog_id).select_related('parent')
        return Comment.objects.all().select_related('parent')

    def perform_create(self, serializer):  
        blog_id = self.kwargs.get('blog_pk')  
        blog = Blog.objects.filter(id=blog_id).first()  
        if blog:  
            parent_id = self.request.data.get('parent')  
            parent_comment = Comment.objects.filter(id=parent_id).first() if parent_id else None  
            if parent_comment and parent_comment.parent is not None:  
                raise ValidationError("Parent comment is a reply to another comment.")  
            if parent_comment and parent_comment.blog != blog:  
                raise ValidationError("Replies must belong to the same blog as the parent comment.")  
            serializer.save(blog=blog, parent=parent_comment)  
        else:  
            raise ValidationError("Cannot create comment without specifying a valid blog.")


    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            if instance.parent:
                instance.parent.replies.remove(instance)
            super().destroy(request, *args, **kwargs)
        except Comment.DoesNotExist:
            raise APIException("Comment not found.")
        except Exception as e:
            raise APIException("An error occurred while processing your request.")