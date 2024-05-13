from rest_framework import serializers
from .models import Post, Rating
from blog.queries import get_post_average_rating, get_post_ratings_count


class PostSerializer(serializers.ModelSerializer):
    """
    This serializer is to serialize the posts data. It is a model serializer that
    serialize data based on Post model. Also it has 3 method serializer to return
    average_rating and rating_count and user_rating values.
    The to_representation method has overriden to show user_rating only if they already
    rated the post and if not, this field won't show.

    """

    average_rating = serializers.SerializerMethodField()
    rating_count = serializers.SerializerMethodField()
    user_rating = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_average_rating(self, obj):
        return get_post_average_rating(obj)["rating__avg"]

    def get_rating_count(self, obj):
        return get_post_ratings_count(obj)["rating__count"]

    def get_user_rating(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            rating = Rating.objects.filter(post=obj, user=user).first()
            if rating:
                return rating.rating
        return None

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if 'user_rating' in data and data['user_rating'] is None:
            del data['user_rating']
        return data


class RatingSerializer(serializers.ModelSerializer):
    """
    This is a model serializer based on Rating Model.
    """

    class Meta:
        model = Rating
        fields = "__all__"
