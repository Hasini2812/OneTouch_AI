CONTACTS = {

    "mom": {
        "phone": "917386347040",
        "email": "nagashanthi786@gmail.com"
    },

    "dad": {
        "phone": "919393370642",
        "email": "rajeshyadav786@gmail.com"
    },

    "geethika": {
        "phone": "918309951188",
        "email": "arrurigeethika06@gmail.com"
    },

    "akshitha": {
        "phone": "918309790084",
        "email": "cingajogiakshitha@gmail.com"
    }
}


def find_contact(name):

    if not name:
        return None

    name = name.strip().lower()

    # Exact match
    if name in CONTACTS:
        return CONTACTS[name]

    # Common spelling variations
    aliases = {
        "geetika": "geethika",
        "geethika": "geethika",
        "akshita": "akshitha"
    }

    if name in aliases:
        return CONTACTS.get(aliases[name])

    # Partial match
    for contact_name, contact_data in CONTACTS.items():

        if (
            name.startswith(contact_name)
            or contact_name.startswith(name)
        ):
            return contact_data

    return None