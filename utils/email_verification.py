import re

EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"


def is_valid_email(email):
    return re.fullmatch(EMAIL_REGEX, email)
