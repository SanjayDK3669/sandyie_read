import traceback

class SandyieException(Exception):
    """
    Custom exception that wraps any error and provides
    a human-friendly explanation along with technical info.
    """
    def __init__(self, message=None, original_exception=None):
        base_message = "[SandyieError] "

        if original_exception:
            # Extract original traceback info
            trace = traceback.format_exc()
            detailed = f"{type(original_exception).__name__}: {str(original_exception)}"
            full_message = f"{base_message}{message or 'An error occurred.'}\nCause: {detailed}\nTraceback:\n{trace}"
        else:
            full_message = base_message + (message or "An unknown error occurred.")

        super().__init__(full_message)
