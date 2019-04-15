from api.location.models import Location


def check_and_add_location(location_name):
    location = Location.query.filter_by(name=location_name).first()
    if not location:
        location_data = Location(name=location_name)
        location_data.save()
