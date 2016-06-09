# from django.contrib.auth.models import User
# from django.core.urlresolvers import reverse
# from django.utils import timezone
# from django.test import TestCase

# from rest_framework import status
# from rest_framework.test import APITestCase

# from .models import Calculation
# from restcalc import views

# class UserTests(APITestCase):
#     def test_create_user(self):
#         """
#         Ensure we can create a new user object.
#         """
#         url = reverse('users')
#         data = {'owner': 'me'}
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Account.objects.count(), 1)
#         self.assertEqual(Account.objects.get().owner, 'me')

