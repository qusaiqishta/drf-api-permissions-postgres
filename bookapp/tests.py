from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Book

# Create your tests here.
class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='testuser', password='password')
        test_user.save()

        test_post = Book.objects.create(
            author = test_user,
            title = 'what not to do if you turn invisible',
            isbn = 'TY78569157128'
        )
        test_post.save()

    def test_blog_content(self):
        post = Book.objects.get(id=2)
        actual_author = str(post.author)
        actual_title = str(post.title)
        actual_isbn = str(post.isbn)
        self.assertEqual(actual_author, 'Ross Welford')
        self.assertEqual(actual_title, 'what not to do if you turn invisible')
        self.assertEqual(actual_isbn, 'TY78569157128')