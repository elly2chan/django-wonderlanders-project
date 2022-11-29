from django.test import TestCase

from wonderlanders.posts.forms import CommentForm


class EditPostFormTests(TestCase):
    def test_comment_post_form_labels_removed__when_all__expect_all_to_be_removed(self):
        form = CommentForm()
        labels = {
            name: field.label
            for name, field in form.fields.items()
        }

        self.assertEqual(
            '',
            labels['comment'],
        )
