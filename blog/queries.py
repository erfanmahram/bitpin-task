from blog.models import Rating
from django.db.models import Avg, Count, FloatField
from django.db.models.functions import Coalesce


def get_post_average_rating(post):
    """
    This query is used to get average rating of the given post
    """

    return Rating.objects.filter(post=post).aggregate(rating__avg=Coalesce(Avg("rating"), 0, output_field=FloatField()))


def get_post_ratings_count(post):
    """
    This query is used to count ratings of the given post
    """

    return Rating.objects.filter(post=post).aggregate(Count("rating"))
