# Generated by Django 4.1.3 on 2022-11-24 18:21

import django.core.validators
from django.db import migrations, models
import wonderlanders.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(error_messages={'max_length': 'First name must be a maximum of 30 characters.', 'min_length': 'First name must be at least 3 characters long.'}, max_length=30, validators=[django.core.validators.MinLengthValidator(3), wonderlanders.core.validators.name_and_title_validator])),
                ('last_name', models.CharField(error_messages={'max_length': 'Last name must be a maximum of 30 characters.', 'min_length': 'Last name must be at least 3 characters long.'}, max_length=30, validators=[django.core.validators.MinLengthValidator(3), wonderlanders.core.validators.name_and_title_validator])),
                ('subject', models.CharField(error_messages={'max_length': 'Subject must be a maximum of 30 characters.', 'min_length': 'Subject must be at least 3 characters long.'}, max_length=30, validators=[django.core.validators.MinLengthValidator(3), wonderlanders.core.validators.name_and_title_validator])),
                ('email', models.EmailField(error_messages={'max_length': 'Email must be a maximum of 250 characters.', 'min_length': 'Email must be at least 3 characters long.'}, max_length=250)),
                ('message', models.CharField(error_messages={'max_length': 'Your message must be a maximum of 250 characters.', 'min_length': 'Your message must be at least 10 characters long.'}, max_length=250, validators=[django.core.validators.MinLengthValidator(10)])),
                ('answered', models.BooleanField(default=False)),
            ],
        ),
    ]
