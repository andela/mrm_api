import datetime

from .credentials import Credentials


class RoomSchedules(Credentials):
    """Create and get room schedules
       :methods
           create_room_event_schedules
           get_room_event_schedules
    """

    # define schedule methods here
    def get_room_schedules(self, calendar_id, days):
        """ Get room schedules. This method is responsible
            for getting all the events on a rooms calendar.
         :params
            - calendar_id
            - days(Time limit for the schedule you need)
        """

        service = Credentials.set_api_credentials(self)
        # 'Z' indicates UTC time
        now = datetime.datetime.utcnow().isoformat() + 'Z'

        new_time = (
            datetime.datetime.now() + datetime.timedelta(days=days)
            ).isoformat() + 'Z'

        events_result = service.events().list(
            calendarId=calendar_id,
            timeMin=now,
            timeMax=new_time,
            singleEvents=True,
            orderBy='startTime').execute()

        calendar_events = events_result.get('items', [])
        output = []
        if not calendar_events:
            return('No upcoming events found.')
        for event in calendar_events:
            event_details = {}
            event_details["start"] = event['start'].get('dateTime', event['start'].get('date'))  # noqa: E501
            event_details["summary"] = event.get("summary")
            output.append(event_details)
        return output
