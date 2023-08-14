from django.db import models


# Create model of contact.
class Contact(models.Model):
    name = models.CharField(max_length=20, unique=True)
    phone_number = models.EmailField(unique=True)

    is_auto_generated = models.BooleanField(
        blank=False,
        default=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    modified_at = models.DateTimeField(
        auto_now=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"{self.name}"
