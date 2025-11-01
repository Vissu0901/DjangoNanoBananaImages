from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now, customize the response data for ValidationErrors.
    if response is not None and response.status_code == 400:
        error_data = response.data
        # Try to find the first error message to display.
        for field, messages in error_data.items():
            if isinstance(messages, list) and messages:
                response.data = {'detail': f'{field.replace("_", " ").capitalize()}: {messages[0]}'}
                break
            elif isinstance(messages, str):
                 response.data = {'detail': messages}
                 break

    return response
