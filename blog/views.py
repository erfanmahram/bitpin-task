from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Rating
from .serializers import PostSerializer, RatingSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class PostListView(APIView):
    """
    This View is used to get list of posts with their rating and content and title and
    created time

    """

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(login_required, name='dispatch')
class RatePostView(APIView):
    """
    This View is used to post a rating.
    It needs a logged in user and post_id from url params and rating value that is in
    post data.
    if user already voted, the new rating will update the previous rating value.
    """

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        rating_value = request.data.get('rating')
        user = request.user
        rating_instance, created = Rating.objects.get_or_create(
            user=user,
            post_id=post_id,
            defaults={"rating": rating_value},
        )

        # Create or update the rating object using the serializer
        serializer = RatingSerializer(
            instance=rating_instance,
            data={
                "user": user.id,
                "rating": rating_value,
                "post": post_id,
            },
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if created else status.HTTP_200_OK
            )
