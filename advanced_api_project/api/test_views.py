from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.author = Author.objects.create(name='John Doe')
        self.book = Book.objects.create(title='Sample Book', publication_year=2020, author=self.author)
        self.client.login(username='testuser', password='password123')

    def test_create_book(self):
        url = reverse('book-list')  # Adjust the URL name as needed
        data = {'title': 'New Book', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.latest('id').title, 'New Book')

    def test_get_book(self):
        url = reverse('book-detail', args=[self.book.id])  # Adjust the URL name as needed
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])  # Adjust the URL name as needed
        data = {'title': 'Updated Book', 'publication_year': 2021}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])  # Adjust the URL name as needed
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permissions(self):
        # Test for non-authenticated user
        self.client.logout()
        url = reverse('book-list')  # Adjust the URL name as needed
        response = self.client.post(url, {'title': 'Another Book', 'publication_year': 2023, 'author': self.author.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
