from rest_framework.test import APITestCase
from rest_framework import status # we can return request status codes using status 
from django.urls import reverse # will call a URL
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "username": "testcase",
            "email": "testcase@example.com",
            "pasword": "NewPassword@123",
            "password2": "NewPassword@123"
        }

        response = self.client.post(reverse('register'), data) # we are making a client request is post request to our route with test data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):

    def setUp(self): # the basic setup for testing. For example we might create a test user here and then test login.
        self.user = User.objects.create_user(username="testuser", password="NewPassword@123")

    def test_login(self):
        data = {
            "username": "testuser",
            "password": "NewPassword@123"
        }

        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
        self.token = Token.objects.get(user__username="testuser") # a token is created by Django Signals whenever a user is created so we get that token
        # The credentials method can be used to set headers that will then be included on all subsequent requests by the test client. Other words: logging user with token
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) 
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK) # the view that logs out user returns a 200 ok code.