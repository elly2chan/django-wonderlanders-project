from django.test import TestCase

from wonderlanders.common.forms import ContactForm


class ContactFormTests(TestCase):
    def test_contact_form_labels_removed__when_all__expect_all_to_be_removed(self):
        form = ContactForm()
        labels = {
            name: field.label
            for name, field in form.fields.items()
        }

        self.assertEqual(
            '',
            labels['first_name'],
        )
        self.assertEqual(
            '',
            labels['last_name'],
        )
        self.assertEqual(
            '',
            labels['subject'],
        )
        self.assertEqual(
            '',
            labels['email'],
        )
        self.assertEqual(
            '',
            labels['message'],
        )

    def test_contact_form_placeholders_added__when_all__expect_all_to_be_added(self):
        form = ContactForm()
        placeholders = {
            name: field.widget.attrs['placeholder']
            for name, field in form.fields.items()
        }

        self.assertEqual(
            'FIRST NAME',
            placeholders['first_name'],
        )
        self.assertEqual(
            'LAST NAME',
            placeholders['last_name'],
        )
        self.assertEqual(
            'SUBJECT',
            placeholders['subject'],
        )
        self.assertEqual(
            'EMAIL',
            placeholders['email'],
        )
        self.assertEqual(
            'MESSAGE',
            placeholders['message'],
        )

    def test_contact_form_style_and_class_added__when_all__expect_all_to_be_added(self):
        form = ContactForm()
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
            field_class['first_name'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['first_name'],
        )
        self.assertEqual(
            'form-control',
            field_class['last_name'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['last_name'],
        )
        self.assertEqual(
            'form-control',
            field_class['subject'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['subject'],
        )
        self.assertEqual(
            'form-control',
            field_class['email'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['email'],
        )
        self.assertEqual(
            'form-control',
            field_class['message'],
        )
        self.assertEqual(
            'max-width: 300px; resize: none',
            field_style['message'],
        )
