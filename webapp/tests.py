from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import myModel  # Import your model
class MyModelViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create some initial data for testing
        self.data = {'name': 'value1', 'description': 'value2'}
        self.model = myModel.objects.create(**self.data)

    def test_list_view(self):
        # Test GET request to list all objects
        response = self.client.get('/model/?format=json')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)  # Check if one object is returned

    def test_detail_view(self):
        # Test GET request to retrieve a single object
        response = self.client.get(f'/model/{self.model.id}/')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.data['name'])  # Check if data matches

    def test_create_view(self):
        # Test POST request to create a new object
        new_data = {'name': 'new_value1', 'description': 'new_value2'}
        response = self.client.post('/model/', new_data, format='json')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Check if the object was created in the database
        self.assertTrue(myModel.objects.filter(name='new_value1').exists())

    def test_update_view(self):
        # Test PUT request to update an existing object
        updated_data = {'name': 'updated_value1', 'description': 'updated_value2'}
        response = self.client.put(f'/model/{self.model.id}/', updated_data, format='json')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the object was updated in the database
        self.model.refresh_from_db()
        self.assertEqual(self.model.name, 'updated_value1')

    def test_delete_view(self):
        # Test DELETE request to delete an existing object
        response = self.client.delete(f'/model/{self.model.id}/')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Check if the object was deleted from the database
        self.assertFalse(myModel.objects.filter(id=self.model.id).exists())
