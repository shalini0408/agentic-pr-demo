import unittest
from app.auth import validate_username


class UsernameValidationTests(unittest.TestCase):
    def test_valid_username(self):
        self.assertTrue(validate_username("alice_123"))

    def test_short_username(self):
        self.assertFalse(validate_username("ab"))

    def test_spaces_not_allowed(self):
        self.assertFalse(validate_username("alice smith"))

    def test_long_username(self):
        self.assertFalse(validate_username("a" * 21))

    def test_non_string(self):
        self.assertFalse(validate_username(None))


if __name__ == "__main__":
    unittest.main()
