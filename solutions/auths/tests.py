from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status

# Create your tests here.
class AccountsTest(APITestCase):
	def setUp(self):
		'''originally create a user'''
		self.test_user=User.objects.create_user('testuser','test@gmail.com','testpassword')
		'''url for creating an account'''
		self.create_url=reverse('account-create')

	def test_create_user(self):
		data={
		'username':'joan',
		'email':'joan@gmail.com',
		'password':'mypassword'
		}
		response=self.client.post(self.create_url,data,format='json')
		'''make sure we have two users in the database'''
		self.assertEqual(User.objects.count(),2)
		self.assertEqual(response.status_code,status.HTTP_201_CREATED)
		'''assert for return of username and email upon successful creation'''
		self.assertEqual(response.data['username'],data['username'])
		self.assertEqual(response.data['email'],data['email'])
		# self.assertFalse('password' in response.databases)

	def test_create_user_with_empty_password(self):
		data = {
				'username': 'joan',
				'email': 'joan@gmail.com',
				'password': ''
		}

		response = self.client.post(self.create_url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(User.objects.count(), 1)
		self.assertEqual(len(response.data['password']), 1)
