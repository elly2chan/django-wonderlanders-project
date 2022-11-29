import tempfile

from tests.posts.utils.base_test_case import BaseTestCase
from wonderlanders.posts.models import Post


class PostModelTests(BaseTestCase):

    def test_post_save__when_all_is_valid__expect_correct_result(self):
        self.assertIsNotNone(self.post.pk)

    def test_post_save__when_title_is_invalid__expect_exception(self):
        post = Post(
            title="Test Post ",
            image=tempfile.NamedTemporaryFile(suffix=".jpg").name,
            destination='Wonderland',
            description='Test description',
            category=self.post_category,
            user=self.user,
        )

        post.full_clean()
        post.save()

        self.assertIsNotNone(post.pk)

        # TODO: Fix this when you add Cloudinary fields
        # print(post.image.path)