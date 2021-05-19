from django.db import models

from check.checker import Checker

# Create your models here.
class Online(models.Model):
    UP = 0
    DOWN = 1
    
    STATUSES = (
        (UP, "Up"),
        (DOWN, "Down")
    )

    status = models.PositiveSmallIntegerField(choices=STATUSES, default=DOWN)
    
    created_on = models.DateTimeField(verbose_name="Created", auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

class Website(models.Model):
    url = models.URLField()

    created_on = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated_on = models.DateTimeField(verbose_name="Updated", auto_now=True)

    statuses = models.ManyToManyField(Online, related_name="statuses")

    @property
    def client(self) -> Checker:
        return Checker(self.url)

    def update_status(self) -> None:
        if self.client.status_code == 200:
            self.statuses.create(status=Online.UP)
        else:
            self.statuses.create(status=Online.DOWN)
        
