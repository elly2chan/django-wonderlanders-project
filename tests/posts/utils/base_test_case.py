import tempfile

from django.test import TestCase

from tests.utils.create_user import create_user
from wonderlanders.posts.models import PostCategory, Post


class BaseTestCase(TestCase):
    def setUp(self):
        self.user = create_user()
        self.post_category = PostCategory(title="Postcards", user=self.user, )
        self.post_category.save()

        self.post = Post.objects.create(
            title="Test Delete Post",
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            destination='Wonderland',
            description='Test description',
            category=self.post_category,
            user=self.post_category.user,
        )

    def assertCollectionEmpty(self, collection, message=None):
        return self.assertEqual(0, len(collection), message)

