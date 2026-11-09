from django.test import SimpleTestCase
from django.urls import reverse


class ViewTests(SimpleTestCase):
    def test_home_view_returns_hello_world(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Hello, World!')

    def test_about_view_returns_about_page(self):
        response = self.client.get(reverse('about'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'About Page')
        
    def test_settings_view_returns_settings_page(self):
        response = self.client.get(reverse('settings'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Settings Page')