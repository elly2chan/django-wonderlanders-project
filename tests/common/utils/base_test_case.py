from django.test import TestCase


class BaseTestCase(TestCase):
    def assertCollectionEmpty(self, collection, message=None):
        return self.assertEqual(0, len(collection), message)
