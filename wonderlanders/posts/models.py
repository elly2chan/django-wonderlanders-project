import cloudinary.uploader
from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.text import slugify


from wonderlanders.core.validators import name_and_title_validator

UserModel = get_user_model()


class PostCategory(models.Model):
    class Meta:
        verbose_name_plural = 'Post Categories'

    MAX_TITLE_LENGTH = 15
    MIN_TITLE_LENGTH = 3

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=(MinLengthValidator(MIN_TITLE_LENGTH), name_and_title_validator),
        error_messages={
            'max_length': f'Category title must be a maximum of {MAX_TITLE_LENGTH} characters.',
            'min_length': f'Category title must be at least {MIN_TITLE_LENGTH} characters long.',
        },
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.title}'.replace(' ', '-'))

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title


def get_photo_name_by_post_name(instance):
    return 'post_{}'.format(instance.title).lower().replace(' ', '_')


class Post(models.Model):
    MAX_TITLE_LENGTH = 20
    MIN_TITLE_LENGTH = 3
    MAX_DESTINATION_LENGTH = 30
    MIN_DESTINATION_LENGTH = 3
    MAX_DESCRIPTION_LENGTH = 550
    MIN_DESCRIPTION_LENGTH = 5

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
        validators=(MinLengthValidator(MIN_TITLE_LENGTH), name_and_title_validator),
        error_messages={
            'max_length': f'Post title must be a maximum of {MAX_TITLE_LENGTH} characters.',
            'min_length': f'Post title must be at least {MIN_TITLE_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    photo = CloudinaryField(
        folder='mediafiles/post_photos',
        public_id=get_photo_name_by_post_name,
        null=False,
        blank=False,
    )

    destination = models.CharField(
        max_length=MAX_DESTINATION_LENGTH,
        validators=(MinLengthValidator(MIN_DESTINATION_LENGTH), ),
        error_messages={
            'max_length': f'Destination must be a maximum of {MAX_DESTINATION_LENGTH} characters.',
            'min_length': f'Destination must be at least {MIN_DESTINATION_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=MAX_DESCRIPTION_LENGTH,
        validators=(MinLengthValidator(MIN_DESCRIPTION_LENGTH), ),
        error_messages={
            'max_length': f'Description must be a maximum of {MAX_DESCRIPTION_LENGTH} characters.',
            'min_length': f'Description must be at least {MIN_DESCRIPTION_LENGTH} characters long.',
        },
        null=False,
        blank=False,
    )

    category = models.ForeignKey(
        PostCategory,
        on_delete=models.CASCADE,
        default='',
        null=False,
        blank=False,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.title


@receiver(pre_delete, sender=Post)
def photo_auto_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.photo.public_id)


class PostComment(models.Model):
    MAX_COMMENT_LENGTH = 300

    comment = models.CharField(
        max_length=MAX_COMMENT_LENGTH,
        error_messages={
            'max_length': f'Comment must be a maximum of {MAX_COMMENT_LENGTH} characters.',
        },
        null=False,
        blank=False,
    )

    publication_datetime = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )
