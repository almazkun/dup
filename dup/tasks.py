from dup.models import Website


def check_all_websites():
    for website in Website.objects.all():
        check_website(website.pk)


def check_website(website_pk: int) -> None:
    website = Website.objects.get(pk=website_pk)
    website.update_status()
