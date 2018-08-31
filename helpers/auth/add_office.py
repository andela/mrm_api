def verify_attributes(kwargs):
    attr_to_check = [
        'name', 'capacity', 'floor_id',
    ]
    for attr in attr_to_check:
        if not kwargs.get(attr):
            raise AttributeError(attr + " is required field")
