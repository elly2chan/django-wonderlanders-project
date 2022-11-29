from django.core.exceptions import ValidationError


def name_and_title_validator(value):
    for ch in value:
        if not ch.isalpha() and not ch.isspace() and not ch == '-':
            raise ValidationError('This field should consist of letters, spaces and dashes only.')

    if value[-1].isspace() or value[-1] == '-':
        raise ValidationError('This field should end with a letter.')

    if value[0].isspace() or value[0] == '-':
        raise ValidationError('This field should start with a letter.')


def username_validator(value):
    min_letters = 3
    found_letters = 0
    for ch in value:
        if not ch.isalnum() and ch not in ['_', '-']:
            raise ValidationError('Username must consist of letters, numbers, underscores and dashes only.')
        elif ch.isalpha():
            found_letters += 1

    if found_letters < min_letters:
        raise ValidationError('Username must have at least three letters.')

    if not value[0].isalpha():
        raise ValidationError('Username must start with a letter.')

    if not value[-1].isalnum():
        raise ValidationError('Username must end with a letter or a number.')


def only_digits_validator(value):
    for ch in value:
        if not ch.isnumeric():
            raise ValidationError('This field must contain only digits.')
