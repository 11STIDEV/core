from django.test import TestCase
from django.contrib.auth.models import User


class UserTestCase(TestCase, ):

    def setUp(self) -> None:
        self.first_user = User.objects.create_user(
            username='francisco', email='email@example.com',
            password='Admins3t4p3@',
        )
        self.user = User

    def test_if_model_return_email_and_name(self, ):
        self.assertEqual(
            str(self.user.objects.get(username='francisco')), 'francisco'
        )
