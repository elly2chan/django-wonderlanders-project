from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.products.utils.base_test_case import BaseTestCase

UserModel = get_user_model()


class EditProductViewTests(BaseTestCase):

    def test_edit_product_view__when_user_is_authenticated_and_user_is_staff__expect_to_show_correct_results(self):
        user = self.user
        user.is_staff = True
        self.client.force_login(user)
        response = self.client.get(reverse('edit product', kwargs={'pk': self.product.pk}))
        self.assertRedirects(response, '/')

    def test_edit_post_view__when_user_is_authenticated_and_user_is_not_staff__expect_redirect_to_index(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('edit product', kwargs={'pk': self.product.pk}))
        self.assertRedirects(response, reverse('index'))

    def test_edit_product_view__when_post_pk_is_not_existent_and_user_is_authenticated_and_user_is_staff__expect_404(self):
        user = self.user
        user.is_staff = True
        self.client.force_login(user)
        response = self.client.get('edit product', kwargs={'pk': self.product.pk + 1})
        self.assertEqual(404, response.status_code)

    def test_edit_product_view__when_post_pk_is_not_existent_and_user_is_authenticated_and_user_is_not_staff__expect_to_redirect_to_index(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('edit product', kwargs={'pk': self.product.pk + 1}))
        self.assertRedirects(response, reverse('index'))

    def test_edit_product_view__when_post_pk_is_not_existent_and_user_is_not_authenticated__expect_to_redirect_to_index(self):
        response = self.client.get(reverse('edit product', kwargs={'pk': self.product.pk + 1}))
        self.assertRedirects(response, reverse('index'))
