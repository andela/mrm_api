
from flask import make_response


class WriteFile():
    """Write analytics report on files
       :methods
           wrte_csv
    """

    def wrte_csv(self, combined_report, file_name):
        '''
        Write analytic report on csv file
        '''
        response = str()
        for title, specific_report_df in combined_report.items():
            response += '{}\n'.format(title)
            response += specific_report_df.to_csv(index=False)
            response += '\n'
        response = make_response(response)
        response.headers['Content-Disposition'] = 'attachment; filename={}'.format(file_name)  # noqa: E501
        response.mimetype = 'text/csv'
        return response
