from django.test import TestCase, Client

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


class TestViews(TestCase):
    def setUp(self):
        self.url = "https://facebbok.com"
        self.c = Client()
        self.c.post("/", data={"url": self.url})

    def test_get(self):
        res = self.c.get("/")

        self.assertTrue(res.status_code, 200)
        self.assertTrue(Website.objects.get(url=self.url))
        self.assertTrue("websites" in res.context)
