from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'description',
            'title',
            'image',

        ]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'post',
            'text',
            'created_date'
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class PostPutSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(default=None)
    created_date = serializers.DateTimeField()
    updated_date = serializers.DateTimeField()
    image = serializers.ImageField(required=False)

    def validate_title(self, title):
        posts = Post.objects.filter(title=title)
        if posts:
            raise ValidationError('This product already exists!!')
        return title