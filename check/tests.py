from django.test import TestCase

from check.checker import Checker

# Create your tests here.
class CheckerTest(TestCase):
    def test_check(self):
        url = "https://google.com"
        c = Checker(url=url)
        self.assertEqual(c.status_code, 200)
