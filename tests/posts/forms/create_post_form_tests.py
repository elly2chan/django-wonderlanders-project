from django.test import TestCase

from wonderlanders.posts.forms import CreatePostForm


class CreatePostFormTests(TestCase):
    def test_create_post_form_labels_removed__when_all__expect_all_to_be_removed_except_category(self):
        form = CreatePostForm()
        labels = {
            name: field.label
            for name, field in form.fields.items()
        }

        self.assertEqual(
            '',
            labels['title'],
        )
        self.assertEqual(
            '',
            labels['image'],
        )
        self.assertEqual(
            '',
            labels['destination'],
        )
        self.assertEqual(
            '',
            labels['description'],
        )
        self.assertEqual(
            'CHOOSE A CONTINENT',
            labels['category'],
        )

    def test_create_post_form_placeholders_added__when_all__expect_all_to_be_added(self):
        form = CreatePostForm()
        placeholders = {
            name: field.widget.attrs['placeholder']
            for name, field in form.fields.items()
        }

        self.assertEqual(
            'TITLE',
            placeholders['title'],
        )
        self.assertEqual(
            'IMAGE',
            placeholders['image'],
        )
        self.assertEqual(
            'DESTINATION',
            placeholders['destination'],
        )
        self.assertEqual(
            'DESCRIPTION',
            placeholders['description'],
        )
        self.assertEqual(
            'CATEGORY',
            placeholders['category'],
        )

    def test_contact_form_style_and_class_added__when_all__expect_all_to_be_added(self):
        form = CreatePostForm()
        field_style = {
            name: field.widget.attrs['style']
            for name, field in form.fields.items()
        }

        field_class = {
            name: field.widget.attrs['class']
            for name, field in form.fields.items()
        }

        self.assertEqual(
            'form-control',
            field_class['title'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['title'],
        )
        self.assertEqual(
            'form-control',
            field_class['image'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['image'],
        )
        self.assertEqual(
            'form-control',
            field_class['destination'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['destination'],
        )
        self.assertEqual(
            'form-control',
            field_class['description'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['description'],
        )
        self.assertEqual(
            'form-control',
            field_class['category'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['category'],
        )
