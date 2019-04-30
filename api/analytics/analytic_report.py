from flask import jsonify, render_template, make_response
import pandas as pd
import pdfkit

from helpers.calendar.analytics_helper import CommonAnalytics

from .write_files import WriteFile


class AnalyticsReport():
    """Get room analytics to export
       :methods
           get_dataframe
           get_all_rooms_summary
           get_least_used_rooms
    """

    def get_dataframe(self, query, rooms_available, start_date, end_date):
        """ Get all rooms data in a dataframe
         :params
            - rooms_available
            - start_date, end_date
        """
        all_rooms_data_df = []
        for room in rooms_available:
            all_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], start_date, end_date)
            if not all_events:
                all_rooms_data_df.append({
                    'roomName': room['name'],
                    'minutes': 0,
                    'summary': None,
                    'attendees': 0
                })
            for event in all_events:
                if event.attendees:
                    event_details = CommonAnalytics.get_event_details(
                        self, query, event, room['calendar_id'])
                    event_details['attendees'] = len(event.attendees)
                    all_rooms_data_df.append(event_details)
        return pd.DataFrame(all_rooms_data_df)

    def get_all_rooms_summary(self, query, start_date, end_date):
        '''
        Get a summarry data for all rooms in a dataframe
        '''
        rooms_available = CommonAnalytics.get_room_details(self, query)
        all_rooms_data_df = AnalyticsReport.get_dataframe(
            self, rooms_available, start_date, end_date)

        rooms_no_meetings_df = all_rooms_data_df.loc[
            lambda all_rooms_data_df: all_rooms_data_df['minutes'] == 0].rename(
                columns={
                    'roomName': 'Room'
                }).assign(Meetings=0)

        rooms_no_meetings_df = rooms_no_meetings_df[['Room', 'Meetings']]

        rooms_with_meeting_df = all_rooms_data_df[
            all_rooms_data_df['minutes'] != 0]['roomName'].value_counts(
            ).rename_axis('Room').reset_index(name='Meetings')
        rooms_summary_df = pd.concat(
            [rooms_no_meetings_df, rooms_with_meeting_df])
        rooms_summary_df['% Share of All Meetings'] = round(
            rooms_summary_df['Meetings'] / rooms_summary_df['Meetings'].sum() *
            100)
        return rooms_summary_df

    def get_least_used_rooms(self, all_rooms_summary_df):
        '''
        Get analytics for the 10 least used rooms
        '''
        sorted_all_rooms_summary_df = all_rooms_summary_df.sort_values(
            'Meetings')
        try:
            tenth_value = sorted_all_rooms_summary_df.loc[10, 'meetings']
            top_ten = sorted_all_rooms_summary_df.loc[sorted_all_rooms_summary_df['meetings'] <= tenth_value]  # noqa
        except KeyError:
            top_ten = sorted_all_rooms_summary_df.head(10)

        return top_ten

    def get_most_used_rooms(self, all_rooms_summary_df):
        '''
        Get analytics for the 10 most used rooms
        '''
        sorted_all_rooms_summary_df = all_rooms_summary_df.sort_values(
            'Meetings', ascending=False)
        try:
            tenth_value = sorted_all_rooms_summary_df.loc[10, 'meetings']
            top_ten = sorted_all_rooms_summary_df.loc[sorted_all_rooms_summary_df['meetings'] >= tenth_value]  # noqa
        except KeyError:
            top_ten = sorted_all_rooms_summary_df.head(10)

        return top_ten

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

    def get_jpeg_analytics_report(self, query, start_time, end_time):
        '''
        Convert analytics for 5 least and most used rooms into a jpeg
        '''
        report_df = AnalyticsReport.generate_combined_analytics_report(
            self, query, start_time, end_time)

        df1 = report_df['Most Used Rooms']
        df2 = report_df['Least Used Rooms']
        report_jpeg = WriteFile.analytics_report_image(self, df1, df2, outputfile="report.jpeg", format="jpeg")  # noqa: E501

        return report_jpeg

    def get_analytics_pdf_reports(self, query, start_date, end_date):
        rendered = AnalyticsReport.write_analytics_to_html(
            self, query, start_date, end_date)

        pdf_file = pdfkit.from_string(rendered, False)
        response = make_response(pdf_file)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'attachment; filename=analytics_report.pdf'  # noqa

        return response

    def get_analytics_html_reports(self, query, start_date, end_date):
        rendered = AnalyticsReport.write_analytics_to_html(
            self, query, start_date, end_date)
        html_string = "{}".format("".join(rendered.splitlines()))

        return jsonify(data=html_string)

    def write_analytics_to_html(self, query, start_date, end_date):
        report_data_frame = AnalyticsReport.generate_combined_analytics_report(
            self, query, start_date, end_date)
        start_date_formatted = CommonAnalytics.format_date(start_date)
        end_date_formatted = CommonAnalytics.format_date(end_date)
        WriteFile.write_to_html_file(
            report_data_frame['Most Used Rooms'],
            report_data_frame['Least Used Rooms'],
            '<h1>Room Analytics Report Summary</h1><p> <h2>Report Period: From ' + start_date_formatted + ' to ' + end_date_formatted + '</h2>',   # noqa
            'templates/analytics_report.html'
            )
        rendered = render_template('analytics_report.html')

        return rendered
