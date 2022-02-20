from django.core.handlers.wsgi import WSGIRequest

from json import loads as json_loads

from typing import Any


# get data from request body (raw)
def get_data(request: WSGIRequest) -> dict:

    body = request.body

    try:
        if body.decode('utf-8') == '':
            body = {}
    except:
        body = {}

    return json_loads(body)


def verify_data(data: Any, required: bool = True, data_type: Any = str,
                min_length: int = None, max_length: int = None,
                min: int = None, max: int = None, error_messages: dict = {}):

    no_need_verify = data is None and not required

    if no_need_verify:
        return True, None

    if required and data is None:
        return False, error_messages.get('required', 'міндетті өріс')

    if data_type and not isinstance(data, data_type):
        return False, error_messages.get('data_type', 'дұрыс емес тип')

    if data_type == str:
        if min_length and len(data) < min_length:
            return False, error_messages.get('min_length', 'минималды ұзындығынан аз')

        if max_length and len(data) > max_length:
            return False, error_messages.get('max_length', 'максималды ұзындығынан артық')

    if data_type == int:
        if min and data < min:
            return False, error_messages.get('min', 'минималды мәннен аз')
        if max and data > max:
            return False, error_messages.get('max', 'максималды мәннен артық')

    return True, None
