import unittest
from strong_random_password_generator.password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_default_settings(self):
        password = generate_password()
        self.assertEqual(len(password), 16)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in "!#$%&*+-?@',./:;=^_~`|<>[](){}" for c in password))

    def test_no_upper(self):
        password = generate_password(use_upper=False)
        self.assertTrue(password.islower())

    def test_no_lower(self):
        password = generate_password(use_lower=False)
        self.assertTrue(password.isupper())

    def test_no_digits(self):
        password = generate_password(use_digits=False)
        self.assertFalse(any(c.isdigit() for c in password))

    def test_no_symbols(self):
        password = generate_password(use_symbols=False)
        self.assertTrue(all(c.isalnum() for c in password))

    def test_add_word(self):
        password = generate_password(add_word="test")
        self.assertIn("test", password)

    def test_begins_with(self):
        password = generate_password(begins_with="pre")
        self.assertTrue(password.startswith("pre"))

    def test_custom_length(self):
        password = generate_password(length=12)
        self.assertEqual(len(password), 12)

    def test_no_similar(self):
        password = generate_password(no_similar=True)
        self.assertFalse(any(c in 'il1Lo0O' for c in password))

    def test_no_duplicate(self):
        password = generate_password(no_duplicate=True)
        self.assertEqual(len(password), len(set(password)))
