from django.urls import reverse

from tests.products.utils.base_test_case import BaseTestCase


class AddProductCategoryViewTests(BaseTestCase):

    def test_add_product_category_view__when_user_is_authenticated_and_not_staff__expect_to_redirect_to_index(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('add product category'))
        self.assertRedirects(response, reverse('index'))

    def test_add_product_category_view__when_user_is_authenticated_and_is_staff__expect_to_add_successfully_and_redirect_to_products(self):
        user = self.user
        user.is_superuser = True
        self.client.force_login(user)
        response = self.client.get(reverse('add product category'))
        self.assertRedirects(response, '/')

    def test_add_product_category_view__when_user_is_not_authenticated__expect_to_redirect_to_index(self):
        response = self.client.get(reverse('add product category'))
        self.assertRedirects(response, reverse('index'))
