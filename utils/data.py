from django.core.handlers.wsgi import WSGIRequest
from json import loads as json_loads


def get_data(request: WSGIRequest) -> dict:

    body = request.body

    try:
        if body.decode('utf-8') == '':
            return {}

        return json_loads(body)
    except:
        return {}


def verify_data(data: any, required: bool = True, data_type: any = str, min_length: int = None, max_length: int = None, error_messages: dict = {}):
    no_need_verify = data is None and not required

    if no_need_verify:
        return True, None

    if required and data is None:
        return False, error_messages.get('required', 'required field')

    if data_type and not isinstance(data, data_type):
        return False, error_messages.get('data_type', 'incorrect type')

    if min_length and len(data) < min_length:
        return False, error_messages.get('min_length', 'less than minimum length')

    if max_length and len(data) > max_length:
        return False, error_messages.get('max_length', 'more than maximum length')

    return True, None
