# For Django
from django.shortcuts import render

# For contacts handling
from apps.contacts.services import generate_contacts


# Get model for data handling
def contacts(request):
    contacts_list = generate_contacts(10)

    return render(
        request=request,
        template_name="contacts/contacts_list.html",
        context={"contacts": contacts_list, "view_name": "contacts"},
    )
