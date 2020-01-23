from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user(self):
        """testing creating user"""
        email = 'test@test.com'
        password = 'Test123456'
        user = get_user_model().objects.create_user(email=email,
                                                    password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_superuser(self):
        """testing creating superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@user.com',
            'some_password'
        )

        self.assertTrue(user.is_superuser)

    def test_email_lower_case(self):
        """testing email be lower case"""
        email = 'sssss@GmIal.COm'
        password = 'asd132456'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email.lower())

    def test_invalid_email(self):
        """testing for invalid email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'asd555')
