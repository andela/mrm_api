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
    """

    def validate_date(self, start_date, end_date):
        '''
        Validate date params
        '''
        try:
            start_date = CommonAnalytics.convert_date(self, start_date)
            end_date = CommonAnalytics.convert_date(self, end_date)
            return (start_date, end_date)
        except ValueError as err:
            raise JsonError(error=str(err), example='Sep 15 2018')

    def validate_request(self):
        '''
        Validate analytics report requests
        '''
        request_data = request.get_json()
        if not all(param in request_data for param in ('start_date', 'end_date')):  # noqa: E501
            return jsonify(
                {"Error": "Request must have start_date and end_date"}
            ), 400
        start_date, end_date = AnalyticsRequest.validate_date(
            self, request_data['start_date'], request_data['end_date'])
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
        query = RoomModel.query
        if file_type == 'CSV':
            response = AnalyticsReport.get_csv_analytics_report(
                self, query, start_date, end_date)
        else:
            response = AnalyticsReport.get_json_analytics_report(
                self, query, start_date, end_date)
        return response
