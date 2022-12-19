import cloudinary.uploader
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.text import slugify

from wonderlanders.core.validators import name_and_title_validator, validate_file_size

UserModel = get_user_model()


class ProductCategory(models.Model):
    class Meta:
        verbose_name_plural = 'product categories'

    MAX_TITLE_LENGTH = 15
    MIN_TITLE_LENGTH = 3

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=(MinLengthValidator(MIN_TITLE_LENGTH), name_and_title_validator),
        error_messages={
            'max_length': f'Category title must be a maximum of {MAX_TITLE_LENGTH} characters.',
            'min_length': f'Category title must be at least {MIN_TITLE_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.title}'.replace(' ', '_'))

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


def get_photo_name_by_product_name(instance):
    return 'product_{}'.format(instance.name).lower().replace(' ', '_')


class Product(models.Model):
    MAX_NAME_LENGTH = 12
    MIN_NAME_LENGTH = 3
    MAX_DESTINATION_LENGTH = 17
    MIN_DESTINATION_LENGTH = 3

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(MinLengthValidator(MIN_NAME_LENGTH), name_and_title_validator),
        error_messages={
            'max_length': f'Product title must be a maximum of {MAX_NAME_LENGTH} characters.',
            'min_length': f'Product title must be at least {MIN_NAME_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    image = CloudinaryField(
        folder='mediafiles/product_photos',
        public_id=get_photo_name_by_product_name,
        validators=(validate_file_size,),
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        default='',
        null=False,
        blank=False,
    )

    destination = models.CharField(
        max_length=MAX_DESTINATION_LENGTH,
        validators=(MinLengthValidator(MIN_DESTINATION_LENGTH), name_and_title_validator),
        error_messages={
            'max_length': f'Destination must be a maximum of {MAX_DESTINATION_LENGTH} characters.',
            'min_length': f'Destination must be at least {MIN_DESTINATION_LENGTH} characters long.',
        },
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.name


@receiver(pre_delete, sender=Product)
def photo_auto_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
