from django.core.urlresolvers import reverse
from django.test import TestCase
from whatsforlunch.search.connect import api_request


class SearchConnectTests(TestCase):

    def test_connect_to_api(self):
        url = {
            'term': 'bars',
            'location': 'sf',
            'limit': 1,
        }
        response = api_request(url_params=url)
        self.assertTrue(response)


class SearchViewTests(TestCase):

    def test_search_view_get(self):
        response = self.client.get(reverse('search'))
        self.assertEquals(response.status_code, 302)


    def test_search_view_post_valid(self):
        data = {
            'latitude': 'toronto',
            'term': 'bars',
        }
        response = self.client.get(reverse('search'), data=data)
        self.assertEquals(response.status_code, 302)
