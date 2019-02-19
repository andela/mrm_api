from flask import request, jsonify
from flask_json import JsonError

from api.room.models import Room as RoomModel
from helpers.calendar.analytics_helper import CommonAnalytics
from .analytic_report import AnalyticsReport


class AnalyticsRequest():
    """Handle analytics requests
       :methods
           validate_date
           validate_request
           get_analytic_report
           get_analytic_report_pdf_file
    """
    def validate_date(self, request_data):
        '''
        Validate date params
        '''
        if 'end_date' not in request_data:
            request_data['end_date'] = None
        try:
            start_date, end_date = CommonAnalytics.convert_dates(
                self, request_data['start_date'], request_data['end_date'])  # noqa: E501
            return (start_date, end_date)
        except ValueError as err:
            raise JsonError(error=str(err), example='Sep 15 2018')

    def validate_request(self):
        '''
        Validate analytics report requests
        '''
        request_data = request.get_json()
        if 'start_date' not in request_data:  # noqa: E501
            return jsonify(
                {"Error": "Request must have a start_date"}
            ), 400
        start_date, end_date = AnalyticsRequest.validate_date(
            self, request_data)
        try:
            file_type = request_data['file_type'].upper()
        except (KeyError, AttributeError):
            file_type = 'JSON'

        return AnalyticsRequest.get_analytic_report(
            self, start_date, end_date, file_type)

    def get_analytic_report(self, start_date, end_date, file_type):
        '''
        Get various analytics
        '''
        query = RoomModel.query.filter(RoomModel.state == 'active')
        if file_type == 'CSV':
            response = AnalyticsReport.get_csv_analytics_report(
                self, query, start_date, end_date)
        elif file_type == 'JPEG':
            response = AnalyticsReport.get_jpeg_analytics_report(
                self, query, start_date, end_date)
        elif file_type == 'PDF':
            response = AnalyticsReport.get_analytics_pdf_reports(
                self, query, start_date, end_date)
        elif file_type == 'HTML':
            response = AnalyticsReport.get_analytics_html_reports(
                self, query, start_date, end_date)

        else:
            response = AnalyticsReport.get_json_analytics_report(
                self, query, start_date, end_date)
        return response
