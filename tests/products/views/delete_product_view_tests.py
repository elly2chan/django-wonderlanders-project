from django.contrib.auth import get_user_model
from django.urls import reverse

from tests.products.utils.base_test_case import BaseTestCase

UserModel = get_user_model()


class DeleteProductViewTests(BaseTestCase):

    def test_delete_product_view__when_user_is_auth_and_user_is_staff__expect_to_redirect_to_products(self):
        user = self.user
        user.is_staff = True
        self.client.force_login(user)
        response = self.client.post(reverse('delete product', kwargs={'pk': self.product.pk}))
        self.assertEqual(302, response.status_code)
        self.assertRedirects(response, '/')

    def test_delete_product_view__when_user_is_auth_and_user_is_not_staff__expect_to_redirect_to_index(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete product', kwargs={'pk': self.product.pk}))
        self.assertRedirects(response, reverse('index'))

    def test_delete_product_view__when_post_pk_is_not_existent_and_user_is_authenticated_and_user_is_not_staff__expect_to_redirect_to_index(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete product', kwargs={'pk': self.product.pk + 1}))
        self.assertRedirects(response, reverse('index'))

    def test_delete_product_view__when_post_pk_is_not_existent_and_user_is_not_authenticated__expect_to_redirect(self):
        response = self.client.get(reverse('delete post', kwargs={'pk': self.product.pk + 1}))
        self.assertEqual(302, response.status_code)
