from django.test import TestCase

from dup.models import Website, Online

# Create your tests here.
class ModelsTest(TestCase):
    def test_model_update_status_up(self):
        url = "https://facebbok.com"
        website = Website.objects.create(url=url)
        website.update_status()

        self.assertTrue(website.statuses.first())
        self.assertTrue(Online.objects.all())

    def test_model_update_status_down(self):
        url = "https://foo.bar"
        website = Website.objects.create(url=url)
        website.update_status()

        self.assertTrue(website.statuses.first())
        self.assertTrue(Online.objects.all())
