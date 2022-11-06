# Custom exceptions go here

class MissingValues(Exception):
    """Raised if a required value is missing

    Attributes:
        missing_values --- require values that are missing
    """

    def __init__(self, values=None):
        self.missing_values = values
        message = f"Missing Values For: {', '.join(value for value in values)}"
        super().__init__(message)
