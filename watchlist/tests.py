from rest_framework.test import APITestCase
from rest_framework import status # we can return request status codes using status 
from django.urls import reverse # will call a URL
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .api.serializers import serializers
from . import models

class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='Password@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        self.stream = models.StreamPlatform.objects.create(
            name="Netflix", description="Test About", website="http://www.amazon.com"
        )

    def test_streamplatform_create(self):
        data = {
            "name": "Netflix",
            "about": "Netflix",
            "website": "http://netflix.com"
        }

        # since streamplatform is a model view set, the routes basename is streamplatform and the list route would be: streamplatform-list
        response = self.client.post(reverse('streamplatform-list'), data) 
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('streamplatform-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_detail(self):
        response = self.client.get(reverse('streamplatform-detail', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WatchListTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='example', password='Password@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        self.stream = models.StreamPlatform.objects.create(
            name="Netflix", description="Test About", website="http://www.amazon.com"
        )

        self.watchlist = models.WatchList.objects.create(
            platform=self.stream,
            title="Example Movie",
            storyline="example storyline",
            active=True
        )

    def test_watchlsit_create(self):
        data = {
            "platform": self.stream,
            "title": "Example Movie",
            "storyline": "example storyline",
            "active": True
        }

        response = self.client.post(reverse('movie-list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
        response = self.client.get(reverse('movie-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_watchlist_detail(self):
        response = self.client.get(reverse('movie-details', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')
        self.assertEqual(models.WatchList.objects.count(), 1)


class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='Password@123')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        self.stream = models.StreamPlatform.objects.create(
            name="Netflix", description="Test About", website="http://www.amazon.com"
        )

        self.watchlist = models.WatchList.objects.create(
            platform=self.stream,
            title="Example Movie",
            storyline="example storyline",
            active=True
        )

        self.watchlist2 = models.WatchList.objects.create(
            platform=self.stream,
            title="Example Movie 2",
            storyline="example storyline",
            active=True
        )

        self.review = models.Review.objects.create(
            review_user = self.user,
            rating = 5,
            description = "Greatest Movie of all times",
            watchlist = self.watchlist2,
            active = True
        )

    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Greatest Movie of all times",
            "watchlist": self.watchlist,
            "active": True
        }

        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_review_create_unauthenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Greatest Movie of all times",
            "watchlist": self.watchlist,
            "active": True
        }

        response = self.client.post(reverse('review-create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Greatest Movie of all times",
            "watchlist": self.watchlist,
            "active": False
        }

        response = self.client.put(reverse('review-detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review-list', args=(self.watchlist2.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_details(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_user_details(self):
        response = self.client.get('/watch/watchlist/reviews/?username=' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)