from django.test import TestCase

from .models import Book  
class BookModelTest(TestCase):

    def setUp(self):
        # Initial test data
        self.book = Book.objects.create(title='Django for Beginners')

    def test_book_title(self):
        self.assertEqual(self.book.title, 'Django for Beginners')
    
    def test_view_url_exists(self):
        response = self.client.get(reversed('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/book_list.html')
