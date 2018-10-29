from flask import jsonify
import pandas as pd

from helpers.calendar.analytics_helper import CommonAnalytics

from .write_files import WriteFile


class AnalyticsReport():
    """Get room analytics to export
       :methods
           get_dataframe
           get_all_rooms_summary
           get_least_used_rooms
    """

    def get_dataframe(self, rooms_available, start_date, end_date):
        """ Get all rooms data in a dataframe
         :params
            - rooms_available
            - start_date, end_date
        """
        all_rooms_data_df = []
        for room in rooms_available:
            calendar_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], start_date, end_date)
            if not calendar_events:
                all_rooms_data_df.append({
                    'RoomName': room['name'],
                    'minutes': None, 'summary': None, 'attendees': 0})
            for event in calendar_events:
                if event.get('attendees'):
                    event_details = CommonAnalytics.get_event_details(self, event, room['calendar_id'])  # noqa: E501
                    event_details['attendees'] = len(event.get('attendees'))
                    all_rooms_data_df.append(event_details)
        return pd.DataFrame(all_rooms_data_df)

    def get_all_rooms_summary(self, query, start_date, end_date):
        '''
        Get a summarry data for all rooms in a dataframe
        '''
        rooms_available = CommonAnalytics.get_calendar_id_name(
            self, query)
        all_rooms_data_df = AnalyticsReport.get_dataframe(
            self, rooms_available, start_date, end_date)
        rooms_summary_df = all_rooms_data_df['roomName'].value_counts().rename_axis(  # noqa: E501
            'Room').reset_index(name='Meetings')
        rooms_summary_df['% Share of All Meetings'] = round(
            rooms_summary_df['Meetings'] / rooms_summary_df['Meetings'].sum() * 100)  # noqa: E501
        return rooms_summary_df

    def get_least_used_rooms(self, all_rooms_summary_df):
        '''
        Get analytics for 5 least used rooms
        '''
        sorted_all_rooms_summary_df = all_rooms_summary_df.sort_values(
            'Meetings')
        return sorted_all_rooms_summary_df.head(5)

    def get_most_used_rooms(self, all_rooms_summary_df):
        '''
        Get analytics for 5 most used rooms
        '''
        sorted_all_rooms_summary_df = all_rooms_summary_df.sort_values(
            'Meetings', ascending=False)
        return sorted_all_rooms_summary_df.head(5)

    def generate_combined_analytics_report(self, query, start_date, end_date):
        '''
        Combine analytics for 5 least and most used rooms
        '''
        all_rooms = AnalyticsReport.get_all_rooms_summary(
            self, query, start_date, end_date)

        least_all_rooms = AnalyticsReport.get_least_used_rooms(
            self, all_rooms)

        most_all_rooms = AnalyticsReport.get_most_used_rooms(
            self, all_rooms)

        response = {
            'Least Used Rooms': least_all_rooms,
            'Most Used Rooms': most_all_rooms
            }
        return response

    def get_json_analytics_report(self, query, start_date, end_date):
        '''
        Convert analytics for 5 least and most used rooms into json format
        '''
        combined_report = AnalyticsReport.generate_combined_analytics_report(
            self, query, start_date, end_date)
        report_json = {key: df.to_dict() for key, df in combined_report.items()}
        return jsonify(report_json)

    def get_csv_analytics_report(self, query, start_date, end_date):
        '''
        Convert analytics for 5 least and most used rooms into a csv
        '''
        combined_report = AnalyticsReport.generate_combined_analytics_report(
            self, query, start_date, end_date)

        summary = WriteFile.wrte_csv(self, combined_report, 'Analytics_report.csv')  # noqa: E501
        return summary
