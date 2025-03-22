from pathlib import Path
import json

from messages import ERROR_MESSAGES, MESSAGES
from found_contact import found_contact
from exceptions import NoFoundContact, input_error

FILENAME = Path(__file__).parent / 'contacts.json'

@input_error
def show_phone(args):
    """ Show phone number by name """
    name = args[0]
    if len(name) < 3:
        return ERROR_MESSAGES['too_short_name']

    contact_exists = found_contact(name)
    if not contact_exists:
        raise NoFoundContact(ERROR_MESSAGES['no_contact'])

    return next(iter(contact_exists.values()))

@input_error
def show_all():
    """ Show all contacts """
    if not FILENAME.exists():
        return None
    try:
        with open(FILENAME, 'r', encoding='utf-8') as file:
            contacts = json.load(file)
            if not contacts:
                return None
            print(contacts)

            return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

    except (FileNotFoundError, json.JSONDecodeError):
        return MESSAGES['contacts_empty']
