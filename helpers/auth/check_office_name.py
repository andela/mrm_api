import re


def check_office_name(office_name):
    return bool(re.match('^(epic\s?towers?||the\s?crest)$',
                         office_name, re.IGNORECASE))


def assert_wing_is_required(office, kwargs):
    if re.match('^(epic\s?towers?)$', office, re.IGNORECASE):
        if not kwargs.get('wing_id'):
            raise AttributeError("wing_id is required for this office")
    else:
        if kwargs.get('wing_id'):
            raise AttributeError("wing_id is not required for this office")
