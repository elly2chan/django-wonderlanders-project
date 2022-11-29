from django.contrib.auth import get_user_model

UserModel = get_user_model()


def create_user():
    user = UserModel.objects.create_user(
        username='elena',
        password='elena123',
        first_name='Elena',
        last_name='Konstantinova',
        email='elena@example.com'
    )
    return user
