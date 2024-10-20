from rest_framework import serializers
from .models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'author', 'content', 'slug', 'image', 'created_at', 'updated_at']
    
    def validate_image(self, value):
        max_size_mb = 5
        if value.size > max_size_mb * 1024 * 1024:
            raise serializers.ValidationError(f"Image size should not exceed {max_size_mb} MB.")
        return value
 
    
class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    parent = serializers.PrimaryKeyRelatedField(queryset=Comment.objects.all(), required=False)
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all(), required=False)

    class Meta:
        model = Comment
        fields = ['id', 'blog', 'author', 'content', 'created_at', 'replies', 'parent']

    def get_replies(self, obj):
        reply_serializer = CommentSerializer(obj.replies.all(), many=True)
        return reply_serializer.data
    
    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        return value
    
    def validate(self, data):  
        parent_comment = data.get('parent')  
        blog = data.get('blog')  
            
        if parent_comment:  
            if not Comment.objects.filter(id=parent_comment.id).exists():  
                raise serializers.ValidationError("Parent comment does not exist.")  
            
            if parent_comment.parent is not None:  
                raise serializers.ValidationError("Parent comment is a reply to another comment.")  
            
            if parent_comment.blog != blog:  
                raise serializers.ValidationError("Replies must belong to the same blog as the parent comment.")  
            
        return data