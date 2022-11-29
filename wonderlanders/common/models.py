from django.core.validators import MinLengthValidator
from django.db import models

from wonderlanders.core.validators import name_and_title_validator


class Contact(models.Model):
    MIN_FIRSTNAME_LENGTH = 3
    MAX_FIRSTNAME_LENGTH = 30
    MIN_LASTNAME_LENGTH = 3
    MAX_LASTNAME_LENGTH = 30
    MIN_SUBJECT_LENGTH = 3
    MAX_SUBJECT_LENGTH = 30
    MIN_EMAIL_LENGTH = 3
    MAX_EMAIL_LENGTH = 250
    MIN_MESSAGE_LENGTH = 10
    MAX_MESSAGE_LENGTH = 250

    first_name = models.CharField(
        max_length=MAX_FIRSTNAME_LENGTH,
        validators=(MinLengthValidator(MIN_FIRSTNAME_LENGTH), name_and_title_validator),
        error_messages={
            'max_length': f'First name must be a maximum of {MAX_FIRSTNAME_LENGTH} characters.',
            'min_length': f'First name must be at least {MIN_FIRSTNAME_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LASTNAME_LENGTH,
        validators=(MinLengthValidator(MIN_LASTNAME_LENGTH), name_and_title_validator),
        error_messages={
            'max_length': f'Last name must be a maximum of {MAX_LASTNAME_LENGTH} characters.',
            'min_length': f'Last name must be at least {MIN_LASTNAME_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    subject = models.CharField(
        max_length=MAX_SUBJECT_LENGTH,
        validators=(MinLengthValidator(MIN_SUBJECT_LENGTH), name_and_title_validator),
        error_messages={
            'max_length': f'Subject must be a maximum of {MAX_LASTNAME_LENGTH} characters.',
            'min_length': f'Subject must be at least {MIN_LASTNAME_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        error_messages={
            'max_length': f'Email must be a maximum of {MAX_EMAIL_LENGTH} characters.',
            'min_length': f'Email must be at least {MIN_EMAIL_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    message = models.CharField(
        max_length=MAX_MESSAGE_LENGTH,
        validators=(MinLengthValidator(MIN_MESSAGE_LENGTH), ),
        error_messages={
            'max_length': f'Your message must be a maximum of {MAX_MESSAGE_LENGTH} characters.',
            'min_length': f'Your message must be at least {MIN_MESSAGE_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    answered = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return f'Send by: {self.email}'
