import sys
from services.room_cancelation.auto_cancel_event import UpdateRecurringEvent
from services.data_deletion.clean_deleted_data_from_db import DataDeletion

services = {
    "clean_database": DataDeletion().clean_deleted_data,
    "autocancel_events": UpdateRecurringEvent().update_recurring_event_status
}


def run_mrm_services(arguments):
    all_services = list(services.keys())
    try:
        if not arguments:
            arguments = list(services.keys())
        for argument in arguments:
            services[argument]()
    except KeyError as wrong_key:
        print(
            wrong_key,
            "is not a valid service. Use one of these",
            all_services
        )


if __name__ == "__main__":
    arguments = sys.argv[1:]
    run_mrm_services(arguments)
