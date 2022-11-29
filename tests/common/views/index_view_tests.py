from django.urls import reverse

from tests.common.utils.base_test_case import BaseTestCase


class IndexViewTests(BaseTestCase):

    def test_index_template_view_expect_emtpy_categories_queryset_and_page_one_of_posts_context(self):
        response = self.client.get(reverse('index'))

        self.assertEqual(response.status_code, 200)
        self.assertCollectionEmpty(response.context['categories'])
        self.assertEqual('<Page 1 of 1>', str(response.context['posts']))

