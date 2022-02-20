from typing import Any
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


def get_user_attr(request, user_obj) -> dict:
    '''user attributes for response'''
    from datetime import datetime

    return {
        'username': user_obj.username,
        'phone': user_obj.phone,
        'is_admin': user_obj.is_admin,
        'birthday': datetime.strftime(user_obj.birthday, '%Y-%m-%d') if user_obj.birthday else None,
        'gender': user_obj.gender,
        'avatar': request.META.get('SERVER_PROTOCOL')[:request.META.get('SERVER_PROTOCOL').find('/')].lower() + '://' + request.META.get('HTTP_HOST') + settings.MEDIA_URL + str(user_obj.avatar),
        'create_time': datetime.strftime(user_obj.create_time, '%Y-%m-%d %H:%M:%S')
    }

def get_user_attr(request, user_obj) -> dict:
    '''user attributes for response'''
    from datetime import datetime

    return {
        'username': user_obj.username,
        'phone': user_obj.phone,
        'is_admin': user_obj.is_admin,
        'birthday': datetime.strftime(user_obj.birthday, '%Y-%m-%d') if user_obj.birthday else None,
        'gender': user_obj.gender,
        'avatar': request.META.get('SERVER_PROTOCOL')[:request.META.get('SERVER_PROTOCOL').find('/')].lower() + '://' + request.META.get('HTTP_HOST') + settings.MEDIA_URL + str(user_obj.avatar),
        'create_time': datetime.strftime(user_obj.create_time, '%Y-%m-%d %H:%M:%S')
    }