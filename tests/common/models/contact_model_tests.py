from django.test import TestCase

from wonderlanders.common.models import Contact


class ContactModelTests(TestCase):
    def test_contact_save__when_all_is_valid__expect_correct_result(self):
        contact_submit = Contact(
            first_name='Elena',
            last_name='Konstantinova',
            subject='Test Subject',
            email='test@example.com',
            message='Test Message',
        )

        contact_submit.full_clean()
        contact_submit.save()

        self.assertIsNotNone(contact_submit.pk)

    def test_contact_save__when_first_name_is_not_valid__expect_exception(self):
        contact_submit = Contact(
            first_name='Elena,',
            last_name='Konstantinova',
            subject='Test Subject',
            email='test@example.com',
            message='Test Message',
        )

        contact_submit.full_clean()
        contact_submit.save()

        self.assertIsNotNone(contact_submit.pk)

    def test_contact_save__when_last_name_is_not_valid__expect_exception(self):
        contact_submit = Contact(
            first_name='Elena',
            last_name='Konstantinova-',
            subject='Test Subject',
            email='test@example.com',
            message='Test Message',
        )

        contact_submit.full_clean()
        contact_submit.save()

        self.assertIsNotNone(contact_submit.pk)

    def test_contact_save__when_subject_is_not_valid__expect_exception(self):
        contact_submit = Contact(
            first_name='Elena',
            last_name='Konstantinova',
            subject=' Test Subject',
            email='test@example.com',
            message='Test Message',
        )

        contact_submit.full_clean()
        contact_submit.save()

        self.assertIsNotNone(contact_submit.pk)
