from django.test import SimpleTestCase
from django.urls import reverse


class BlogTest(SimpleTestCase):

    def test_home_page_status(self):
        self.help_status_code('home')

    def test_home_page_template(self):
        self.help_page_template('home', 'home.html')

    def help_status_code(self, url_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def help_page_template(self, url_name, temp_name):
        url = reverse(url_name)
        response = self.client.get(url)
        self.assertTemplateUsed(response, temp_name)
        self.assertTemplateUsed(response, 'base.html')
