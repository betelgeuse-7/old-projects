import random
import string


def slugify(name):
    lower = name.lower()
    if ' ' in lower:
        no_whitespace = lower.replace(' ', '-')
        Ascii = string.ascii_lowercase + string.ascii_uppercase + string.digits
        insert_random = no_whitespace + '-'
        for i in range(5):
            insert_random += random.choice(Ascii)
        return insert_random
    else:
        Ascii = string.ascii_lowercase + string.ascii_uppercase + string.digits
        insert_random = lower + '-'
        for i in range(5):
            insert_random += random.choice(Ascii)
        return insert_random
