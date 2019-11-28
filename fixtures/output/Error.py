class Error:
    """
        About: Builds an error object for fixtures test
        How to use: import the error_item into the file
                    that needs an error object built.
                    After assigning the prefered values
                    for the error message, location and
                    path, call the build_error method and
                    passing the error_item.
                    (see docstring in build method)
    """

    def __init__(self, **kwargs):
        self.message = kwargs.get('message')
        self.locations = kwargs.get('locations')
        self.path = kwargs.get('path')

    def build_error(self):
        """Builds the error output

        Args:
            self: This the the instance of the class

        Returns:
            An error object of type dictionary
        """
        return {
            "message": self.message,
            "locations": self.locations,
            "path": self.path
        }


error_item = Error
