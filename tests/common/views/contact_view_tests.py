from django.contrib.auth import get_user_model
from django.test import TestCase

from django.urls import reverse

from tests.utils.create_user import create_user

UserModel = get_user_model()


class ContactViewTests(TestCase):

    def test_contact_view__when_no_profile__expect_to_show_correct_template_with_empty_form_fields(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(None, response.context['form']['first_name'].value())
        self.assertEqual(None, response.context['form']['last_name'].value())
        self.assertEqual(None, response.context['form']['email'].value())

    def test_contact_view__when_profile__expect_to_show_initial_values_from_profile_in_form(self):
        self.client.force_login(create_user())
        response = self.client.get(reverse('contact'))
        self.assertEqual('Elena', response.context['form']['first_name'].value())
        self.assertEqual('Konstantinova', response.context['form']['last_name'].value())
        self.assertEqual('elena@example.com', response.context['form']['email'].value())


