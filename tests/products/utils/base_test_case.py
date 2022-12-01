import tempfile

from django.test import TestCase

from tests.utils.create_user import create_user
from wonderlanders.products.models import ProductCategory, Product


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = create_user()
        self.product_category = ProductCategory(title="Postcards", user=self.user, )
        self.product_category.save()

        self.product = Product.objects.create(
            name="Test Product",
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            price=5,
            category=self.product_category,
            destination='Test Destination',
            user=self.product_category.user,
        )

    def assertCollectionEmpty(self, collection, message=None):
        return self.assertEqual(0, len(collection), message)

