from django.db import models


class Contacts(models.Model):
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name}"
