# Generated by Django 3.2.3 on 2021-05-20 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("check", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="website",
            name="statuses",
        ),
        migrations.DeleteModel(
            name="Online",
        ),
        migrations.DeleteModel(
            name="Website",
        ),
    ]
