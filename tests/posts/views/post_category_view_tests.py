from django.urls import reverse

from tests.posts.utils.base_test_case import BaseTestCase


class PostDetailsViewTests(BaseTestCase):

    def test_post_category_view__expect_to_show_correct_template_and_empty_context(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('post category', kwargs={'slug': self.post_category.slug}))
        self.assertEqual(200, response.status_code)
        self.assertTemplateUsed(response, 'posts/post_category.html')
        self.assertEqual(1, len(response.context['posts']))
        self.assertEqual(1, len(response.context['categories']))

    def test_post_category_view__when_pk_is_non_existent__expect_404(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('post category', kwargs={'slug': self.post_category.slug + 'test'}))
        self.assertEqual(404, response.status_code)
