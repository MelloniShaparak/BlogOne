from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
from django.test import TestCase
# Create your tests here.


class BlogTests(TestCase):
    #Creating an object that is a post
    def setUp(self):
        self.user = get_user_model().objects.create(
        username='john',
        email='www.test.com',
        password='pppp'
        )

        self.post = Post.objects.create(
        title='Code every day',
        body='Nice body content',
        author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='This is a title')
        self.assertEqual(str(post),post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}','Code every day')
        self.assertEqual(f'{self.post.author}','john')
        self.assertEqual(f'{self.post.body}','Nice body content')

    def test_post_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Nice body content')
        self.assertTemplateUsed(response,'home.html')
        from django.test import TestCase

    def test_post_detail(self):
        response = self.client.get('/post/1')
        no_response = self.client.get('/post/100000')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'Code every day')
        self.assertTemplateUsed(response,'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),{
        'title':'Nice Title',
        'body':'Nice body',
        'author':'Nice Author',
        })
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Nice Title')
        self.assertContains(response,'Nice body')
        self.assertEqual(response,'Nice Author')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_new',arg='1'),{
        'title':'Updated title',
        'body':'Updated body',
        })

        self.assertEqual(response.status_code,302)

    def test_post_delete_view(self):
        reponse = self.client.post(reverse('post_delete',arg='1'))
        self.assertEqual(response.status_code,302)

    
