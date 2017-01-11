from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
# superlists.lists.views
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

        # expected_html = render_to_string('home.html').strip()
        # print(expected_html)
        # print(response.content.decode())
        # self.assertEqual(response.content.strip().decode(), expected_html)

    def test_home_page_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

        # request = HttpRequest()
        # request.method = 'POST'
        # request.POST['item_text'] = 'A new list item'
        #
        # response = home_page(request)
        # self.assertIn('A new list item', response.content.decode())
        # expected_html = render_to_string(
        #     'home.html',
        #     {'new_item_text': 'A new list item'}
        # ).strip()
        # self.assertTemplateUsed(response, 'home.html')
        # self.assertEqual(response.content.strip().decode(), '')