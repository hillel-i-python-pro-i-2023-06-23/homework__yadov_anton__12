# For python
from collections.abc import Iterator

# Get app model
from apps.contacts.models import Contact
from faker import Faker


# Get contact fields
def get_contact():
    current_faker = Faker()

    current_name = current_faker.name()
    current_phone = current_faker.phone_number()

    return current_name, current_phone

def generate_contact() -> Contact:
    concurrent_credentials = get_contact()

    return Contact(
        name=concurrent_credentials[0],
        phone_number=concurrent_credentials[1],
    )


def generate_contacts(
    amount: int,
) -> Iterator[Contact]:
    for _ in range(amount):
        yield generate_contact()
