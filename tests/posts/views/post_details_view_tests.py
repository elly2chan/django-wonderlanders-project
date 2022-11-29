from django.urls import reverse

from tests.posts.utils.base_test_case import BaseTestCase


class PostDetailsViewTests(BaseTestCase):

    def test_post_details_view__when_user_is_authenticated__expect_to_show_correct_template_and_empty_context(self):
        self.client.force_login(self.post.user)
        response = self.client.get(reverse('post details', kwargs={'pk': self.post.pk}))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'posts/post_details.html')
        self.assertCollectionEmpty(response.context['category_posts'])
        self.assertCollectionEmpty(response.context['post_comments'])
        self.assertEqual(None, response.context['last_comment'])

    def test_post_details_view__when_user_is_not_authenticated__expect_to_redirect(self):
        response = self.client.get(reverse('post details', kwargs={'pk': self.post.pk}))
        self.assertEqual(302, response.status_code)
        self.assertEqual(None, response.context)

    def test_post_details_view__when_user_is_auth_and_pk_is_non_existent__expect_404(self):
        self.client.force_login(self.post.user)
        response = self.client.get(reverse('post details', kwargs={'pk': self.post.pk + 7}))
        self.assertEqual(404, response.status_code)
