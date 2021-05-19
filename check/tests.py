from django.test import TestCase

from check.checker import Checker
from check.models import Website, Online

# Create your tests here.
class CheckerTest(TestCase):
    def test_check(self):
        url = "https://google.com"
        status_code = Checker(url=url)._check()
        self.assertEqual(status_code, 200)

class ModelsTest(TestCase):
    def test_model(self):
        url = "https://facebbok.com"
        website = Website.objects.create(url=url)
        website.update_status()

        self.assertTrue(website.statuses.first())