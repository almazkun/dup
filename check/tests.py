from django.test import TestCase

from check.checker import Checker

# Create your tests here.
class TestChecker(TestCase):
    def test_check(self):
        url = "https://google.com"
        status_code = Checker(url=url)._check()
        self.assertEqual(status_code, 200)
