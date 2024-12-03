from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostTest(TestCase):
    def setUp(self):
        Post.objects.create(title = 'mavzu', text = 'yangilik matni' , text_muallif = "cheklanma")
    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_title = f"{post.title}"
        expected_object_text = f"{post.text}"
        expected_object_text_muallif = f"{post.text_muallif}"
        self.assertEqual(expected_object_title, post.title)
        self.assertEqual(expected_object_text , post.text)
        self.assertEqual(expected_object_text_muallif , post.text_muallif)

class HomePageViewTest(TestCase):
    def setUp(self) :
        Post.objects.create(title = 'mavzu 2', text = 'yangilik matni 2' , text_muallif = "cheklanma")
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
    def test_view_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'home.html')

