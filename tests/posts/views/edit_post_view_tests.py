from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.posts.utils.base_test_case import BaseTestCase

UserModel = get_user_model()


class EditPostViewTests(BaseTestCase):

    def test_edit_post_view__when_user_is_auth_and_user_is_author_of_post__expect_to_show_correct_results(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('edit post', kwargs={'pk': self.post.pk}))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'posts/edit_post.html')
        self.assertEqual(self.user.username, self.post.user.username)

    def test_edit_post_view__when_user_is_auth_and_user_is_superuser__expect_to_show_correct_results(self):
        user = self.user
        user.is_superuser = True
        self.client.force_login(user)
        response = self.client.get(reverse('edit post', kwargs={'pk': self.post.pk}))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'posts/edit_post.html')
        self.assertEqual(self.user.username, self.post.user.username)

    def test_edit_post_view__when_user_is_auth_and_user_is_not_author_of_post__expect_redirect(self):
        new_user = UserModel.objects.create_user(
            username='not_author',
            password='test123',
            first_name='Test',
            last_name='Test',
            email='test@example.com'
        )
        self.client.force_login(new_user)
        response = self.client.get(reverse('edit post', kwargs={'pk': self.post.pk}))
        self.assertEqual(302, response.status_code)

    def test_edit_post_view__when_post_pk_is_not_existent_and_user_is_authenticated__expect_404(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('edit post', kwargs={'pk': self.post.pk + 1}))
        self.assertEqual(404, response.status_code)

    def test_edit_post_view__when_post_pk_is_not_existent_and_user_is_not_authenticated__expect_to_redirect(self):
        response = self.client.get(reverse('edit post', kwargs={'pk': self.post.pk + 1}))
        self.assertEqual(302, response.status_code)
