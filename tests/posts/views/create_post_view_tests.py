from django.test import TestCase
from django.urls import reverse

from tests.posts.utils.base_test_case import create_user


class CreatePostViewTests(TestCase):

    def test_create_post_view__when_user_is_authenticated__expect_to_show_correct_template(self):
        self.client.force_login(create_user())
        response = self.client.get(reverse('create post'))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'posts/create_post.html')

    def test_create_post_view__when_user_is_not_authenticated__expect_to_redirect(self):
        response = self.client.get(reverse('create post'))
        self.assertEqual(302, response.status_code)

    # def test_create_post_view__when_user_is_authenticated__expect_correct_result(self):
    #     self.client.force_login(create_user())
    #     response = self.client.post(reverse('create post'))
    #     self.assertEqual(200, response.status_code)
