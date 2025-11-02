from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    SessionAuthentication without CSRF checks.
    """
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Customize the response data for ValidationErrors.
    if isinstance(exc, ValidationError) and response is not None:
        error_data = response.data
        detail_message = "An unknown error occurred."

        if isinstance(error_data, dict):
            # Handle non_field_errors or other top-level errors
            if 'non_field_errors' in error_data and isinstance(error_data['non_field_errors'], list) and error_data['non_field_errors']:
                detail_message = error_data['non_field_errors'][0]
            else:
                # Try to find the first error message from any field
                for field, messages in error_data.items():
                    if isinstance(messages, list) and messages:
                        detail_message = f'{field.replace("_", " ").capitalize()}: {messages[0]}'
                        break
                    elif isinstance(messages, str):
                        detail_message = messages
                        break
        elif isinstance(error_data, list) and error_data:
            # Handle cases where response.data is a list of strings
            detail_message = error_data[0]

        response.data = {'detail': detail_message}

    return response
