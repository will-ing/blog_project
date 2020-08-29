from .models import Blog
from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class BlogTest(TestCase):

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

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='pass'
        )

        self.blog = Blog.objects.create(
            title='test title',
            author=self.user,
            body='test desc',
        )

    def test_content(self):
        self.assertEqual(self.blog.title, 'test title')
        self.assertEqual(self.blog.author, self.user)
        self.assertEqual(self.blog.body, 'test desc')

    def test_create(self):
        response = self.client.post(reverse('create'), {
            'title': 'test title',
            'author': self.user,
            'body': 'test desc',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test title')
        self.assertContains(response, 'test desc')
        self.assertTemplateUsed(response, 'create.html')

    def test_trip_delete_view(self):
        response = self.client.get(reverse('delete', args='1'))
        self.assertEqual(response.status_code, 200)
