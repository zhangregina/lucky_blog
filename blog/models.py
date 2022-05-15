from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='photo', null=True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,  # при удалении поста, удал комменты
                             related_name='post_comment')
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

