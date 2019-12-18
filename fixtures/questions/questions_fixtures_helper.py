import datetime


def date_maker(offset):
    """Takes in an offset value with unit days and
       creates a datetime object which is offset by
       the value provided

       Args:
          offset: An integer representation of the number
          of days to offset the datetime object

       Returns: A datetime object
    """
    return (
        datetime.datetime.now().replace(microsecond=0) +
        datetime.timedelta(days=offset)
    ).isoformat()


start_date = date_maker(1)
end_date = date_maker(2)
wrong_start_date = date_maker(-1)
wrong_end_date = date_maker(1)
