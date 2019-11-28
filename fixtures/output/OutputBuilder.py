class OutputBuilder():
    """
        About: Builds fixture outputs for tests
        How to use: import the build method and provide
                    the arguments that are required (see
                    docstring in build method) to build
                    the desired output.
    """

    def __init__(self):
        self.errors = []
        self.data = {}
        self.responses = {}

    @staticmethod
    def item():
        return OutputBuilder()

    def in_errors(self, output):
        self.errors.append(output)
        return self

    def in_data(self, output):
        self.data = output
        return self

    def in_responses(self, output):
        self.responses = output
        return self

    def package(self):
        """Packages the output object based on what is provided

        Args:
            self: This the the instance of the class
        Returns:
            A packaged output object of type dictionary
        """
        output_obj = {
            "errors": self.errors,
            "data": self.data,
            "responses": self.responses
        }

        if len(self.errors) == 1 and self.errors[0] is None:
            del output_obj["errors"]
        if self.data is None:
            del output_obj["data"]
        if self.responses is None:
            del output_obj["responses"]

        return output_obj


def build(error=None, data=None, response=None):
    """Builds the output that has been packaged by the package method

    Args:
        error: This is a list of error dictionaries [optional]
        data: A dictionary that forms part of the output object [optional]
        response: A dictionary that forms part of the output object [optional]

    Returns:
        A built output object of type dictionary
    """
    return OutputBuilder.item().in_errors(
        error).in_data(data).in_responses(response).package()
