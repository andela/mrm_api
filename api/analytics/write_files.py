from flask import make_response
import imgkit
import os
import cv2


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

    def analytics_report_image(self, df1, df2, outputfile="report.jpeg", format="jpeg"):  # noqa: E501
        '''
        Returning a DataFrame as a JPEG image.
        '''
        css = """
            <style type=\"text/css\">
            table {
            width: 640px;
            border-collapse:
            collapse;
            border-spacing: 0;
            margin-left:5%
            }

            td, th {
            border: 1px solid transparent; /* No more visible border */
            height: 40px;
            text-align: left;
            }

            th {
            font-weight: bold;
            }

            td {
            background: #FAFAFA;
            padding-left:3%
            }

            table tr:nth-child(odd) td{
            background-color: white;
            }

            h3 {
            margin-left:3% !important;
            }
            </style>
            """
        fn = "file.html"
        try:
            os.remove(fn)
        except:  # noqa: E722
            None

        text_file = open(fn, "a")
        text_file.write(css)
        text_file.write('<br><br><h3>Most Booked Rooms</h3>' + df1.to_html(index=False) + '<br><br><h3>Least Booked Rooms</h3>' + df2.to_html(index=False) + '<br><br>')  # noqa: E501
        text_file.close()

        imgkitoptions = {"format": format}
        imgkit.from_file(fn, "templates/report_template.jpeg", options=imgkitoptions)  # noqa: E501
        os.remove(fn)
        im_gray = cv2.imread('templates/report_template.jpeg')
        img_str = cv2.imencode('.jpg', im_gray)[1].tostring()
        response = make_response(img_str)
        cd = 'attachment; filename=report.jpeg'
        response.headers['Content-Disposition'] = cd
        response.mimetype = 'image/jpeg'
        return response
