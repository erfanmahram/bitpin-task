from rest_framework.test import APITestCase
from django.urls import reverse
from blog.models import Post, Rating, User


class PostTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.client.force_authenticate(user=self.user)
        self.url = reverse("post-list")
        self.post1 = Post.objects.create(title='Test Post 1', content='Test content 1')
        Rating.objects.create(user=self.user, post=self.post1, rating=4)

    def test_get_post_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class RatePostViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
            )
        self.url = reverse("rate-post", kwargs={"post_id": 1})
        self.post = Post.objects.create(title='Test Post', content='Test content')

    def test_rate_post(self):
        self.client.force_login(user=self.user)
        response = self.client.post(self.url, {'rating': 3}, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Rating.objects.first().rating, 3)

    def test_rate_post_twice(self):
        self.client.force_login(user=self.user)
        Rating.objects.create(user=self.user, post=self.post, rating=2)
        response = self.client.post(self.url, {'rating': 4}, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Rating.objects.first().rating, 4)

    def test_rate_post_not_login(self):
        response = self.client.post(self.url, {'rating': 3}, format='json')
        self.assertEqual(response.status_code, 302)

