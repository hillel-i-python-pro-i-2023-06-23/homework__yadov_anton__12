import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contact
from apps.contacts.services import generate_contacts


class Command(BaseCommand):
    help = "Generate contacts"

    # Get parser for command args
    def add_arguments(self, parser) -> None:
        # Set argument with default value
        parser.add_argument(
            "--amount",
            type=int,
            help="Number of contacts to generate",
            default=20,
        )

    def handle(self, *args, **options) -> None:
        amount: int = options["amount"]

        # Log handling to terminal
        logger = logging.getLogger("django")

        # Get queryset template
        queryset = Contact.objects.all()

        logger.info(f"Current amount of contact before: {queryset.count()}")

        for contact in generate_contacts(amount=amount):
            contact.is_auto_generated = True
            contact.save()

        logger.info(f"Current amount of contact after: {queryset.count()}")
