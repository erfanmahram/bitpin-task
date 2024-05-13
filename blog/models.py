from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    This model stores a post instance

    Required Fields:
    title: <str>
    content: <str>

    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    """
    This model stores a Rating instance

    Required Fields:
    user: <user> --> pk of the user model
    post: <post> --> pk of the post model
    rating: <int>

    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(6)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f"{self.user.username} - {self.post.title}: {self.rating}"
