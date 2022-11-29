from tests.posts.utils.base_test_case import BaseTestCase
from wonderlanders.posts.models import PostCategory


class PostCategoryModelTests(BaseTestCase):

    def test_post_category_save__when_all_is_valid__expect_correct_result(self):
        self.assertIsNotNone(self.post_category.pk)
        self.assertEqual(f'{self.post_category.title.lower().replace(" ", "_")}', self.post_category.slug)

    def test_post_category_save__when_title_not_valid__expect_exception(self):
        post_category = PostCategory(
            title=" Postcards",
            user=self.user,
        )
        post_category.full_clean()
        post_category.save()

        self.assertIsNotNone(post_category.pk)
