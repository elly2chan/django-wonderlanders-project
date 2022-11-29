from enum import Enum

from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from wonderlanders.core.model_mixins import ChoicesEnumMixin
from wonderlanders.core.validators import name_and_title_validator, only_digits_validator


UserModel = get_user_model()


class Country(ChoicesEnumMixin, Enum):
    bulgaria = 'Bulgaria'
    serbia = 'Serbia'
    greece = 'Greece'
    romania = 'Romania'
    macedonia = 'Macedonia'


class Order(models.Model):
    MIN_FIRSTNAME_LENGTH = 3
    MAX_FIRSTNAME_LENGTH = 30
    MIN_LASTNAME_LENGTH = 3
    MAX_LASTNAME_LENGTH = 30
    MIN_POSTAL_CODE_LENGTH = 4
    MAX_POSTAL_CODE_LENGTH = 10
    MIN_EMAIL_LENGTH = 3
    MAX_EMAIL_LENGTH = 250
    MIN_ADDRESS_LENGTH = 5
    MAX_ADDRESS_LENGTH = 50
    MIN_CITY_LENGTH = 3
    MAX_CITY_LENGTH = 30
    MIN_PHONE_LENGTH = 5
    MAX_PHONE_LENGTH = 15

    order_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    first_name = models.CharField(
        max_length=MAX_FIRSTNAME_LENGTH,
        validators=(MinLengthValidator(MIN_FIRSTNAME_LENGTH), name_and_title_validator, ),
        error_messages={
            'max_length': f'First name must be a maximum of {MAX_EMAIL_LENGTH} characters.',
            'min_length': f'First name must be at least {MIN_EMAIL_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=MAX_LASTNAME_LENGTH,
        validators=(MinLengthValidator(MIN_LASTNAME_LENGTH), name_and_title_validator,),
        error_messages={
            'max_length': f'Last name must be a maximum of {MAX_EMAIL_LENGTH} characters.',
            'min_length': f'Last name must be at least {MIN_EMAIL_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    postal_code = models.CharField(
        max_length=MAX_POSTAL_CODE_LENGTH,
        validators=(MinLengthValidator(MIN_POSTAL_CODE_LENGTH), only_digits_validator, ),
        error_messages={
            'max_length': f'Postal code must be a maximum of {MAX_POSTAL_CODE_LENGTH} digits.',
            'min_length': f'Postal code must be at least {MIN_EMAIL_LENGTH} digits long.',
        },
        null=False,
        blank=False,
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        validators=(MinLengthValidator(MIN_EMAIL_LENGTH), ),
        error_messages={
            'max_length': f'Email must be a maximum of {MAX_EMAIL_LENGTH} characters.',
            'min_length': f'Email must be at least {MIN_EMAIL_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    address = models.CharField(
        max_length=MAX_ADDRESS_LENGTH,
        validators=(MinLengthValidator(MIN_ADDRESS_LENGTH), ),
        error_messages={
            'max_length': f'Address must be a maximum of {MAX_ADDRESS_LENGTH} characters.',
            'min_length': f'Address must be at least {MIN_ADDRESS_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    city = models.CharField(
        max_length=MAX_CITY_LENGTH,
        validators=(MinLengthValidator(MIN_CITY_LENGTH), name_and_title_validator, ),
        error_messages={
            'max_length': f'City must be a maximum of {MAX_CITY_LENGTH} characters.',
            'min_length': f'City must be at least {MIN_CITY_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    country = models.CharField(
        max_length=Country.max_len(),
        choices=Country.choices(),
        default=Country.bulgaria,
    )

    phone = models.CharField(
        max_length=MAX_PHONE_LENGTH,
        validators=(MinLengthValidator(MIN_PHONE_LENGTH), only_digits_validator, ),
        error_messages={
            'max_length': f'Phone must be a maximum of {MAX_PHONE_LENGTH} characters.',
            'min_length': f'Phone must be at least {MIN_PHONE_LENGTH} digits long.',
        },
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    order_total_price = models.FloatField(
        null=True,
        blank=True,
    )

    order_products_quantity = models.IntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Order: {self.id} | Username: {self.user}'
