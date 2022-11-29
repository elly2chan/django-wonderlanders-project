from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from wonderlanders.core.validators import name_and_title_validator, username_validator


class AppUser(AbstractUser):
    MIN_USERNAME_LENGTH = 3
    MAX_USERNAME_LENGTH = 40
    MIN_FIRSTNAME_LENGTH = 3
    MAX_FIRSTNAME_LENGTH = 30
    MIN_LASTNAME_LENGTH = 3
    MAX_LASTNAME_LENGTH = 30
    MIN_EMAIL_LENGTH = 3
    MAX_EMAIL_LENGTH = 250

    username = models.CharField(
        max_length=MAX_USERNAME_LENGTH,
        validators=(MinLengthValidator(MIN_USERNAME_LENGTH), username_validator),
        error_messages={
            'max_length': f'Username must be a maximum of {MAX_USERNAME_LENGTH} characters.',
            'min_length': f'Username must be at least {MIN_USERNAME_LENGTH} characters long.',
        },
        null=False,
        blank=False,
        unique=True,
    )

    first_name = models.CharField(
        max_length=MAX_FIRSTNAME_LENGTH,
        validators=(MinLengthValidator(MIN_FIRSTNAME_LENGTH), name_and_title_validator, ),
        error_messages={
            'max_length': f'First name must be a maximum of {MAX_FIRSTNAME_LENGTH} characters.',
            'min_length': f'First name must be at least {MIN_FIRSTNAME_LENGTH} characters long.',
        },
        null=False,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LASTNAME_LENGTH,
        validators=(MinLengthValidator(MIN_LASTNAME_LENGTH), name_and_title_validator),
        error_messages={
            'max_length': f'Last name must be a maximum of {MAX_LASTNAME_LENGTH} characters.',
            'min_length': f'Last name must be at least {MIN_LASTNAME_LENGTH} characters long.',
        },
        null=False,
        blank=True,
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        validators=(MinLengthValidator(MIN_EMAIL_LENGTH), ),
        error_messages={
            'max_length': f'Email must be a maximum of {MAX_EMAIL_LENGTH} characters.',
            'min_length': f'Email must be at least {MIN_EMAIL_LENGTH} characters long.',
        },
        unique=True,
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
