from django.test import TestCase
from whatsforlunch.search.connect import api_request


class SearchConnectTests(TestCase):

    def test_connect_to_api(self):
        url = {
            'term': 'bars',
            'location': 'sf',
        }
        response = api_request(url_params=url)
        print response
