
# Create your tests here.
from django.urls import reverse, include, path
from rest_framework import status
from rest_framework.test import APITestCase

class CalcuTests(APITestCase):

    def test_calculation(self):
        """
        Ensure we can create a new account object.
        """
        urlpatterns = [
        path('calculator/', include('calcu.urls')),
        ]


        url = reverse('cart')
        data = {'cart_value': 500 ,
                'delivery_distance':500,    
                'number_of_items': 4,
                'time': '2021-01-16T13:00:00Z',
                }
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.data['deliverey_fees'], 700)
        