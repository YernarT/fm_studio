from django.core.handlers.wsgi import WSGIRequest
from fm_studio import settings
from user.models import User
from datetime import datetime, timedelta
from cryptocode import encrypt, decrypt


def verify_token(request: WSGIRequest):
    token = request.headers.get('X-AUTH-TOKEN', '')
    payload = decrypt(token, settings.SECRET_KEY)

    if token and payload:
        id, token_expire_date = payload.split('.')
        token_expire_date = datetime.strptime(token_expire_date, '%Y%m%d%H%M')
        now = datetime.now()

        # not expired
        if (now - token_expire_date).days < 0:
            user = User.objects.get(id=id)

            user_obj = {
                'id': user.id,
                'username': user.username,
                'phone': user.phone,
                'is_admin': user.is_admin,
                'birthday': user.birthday,
                'gender': user.gender,
                'avatar': request.META.get('SERVER_PROTOCOL')[:request.META.get('SERVER_PROTOCOL').find('/')].lower()  + '://' + request.META.get('HTTP_HOST') + settings.MEDIA_URL + str(user.avatar),
                'create_time': user.create_time
            }

            return True, {'message': 'Verification succeeded', 'data': {'user_attr': user_obj,
                                                                        'user': user
                                                                        }}
        else:
            return False, {'message': 'Token expired'}

    return False, {'message': 'Token incorrect'}


def generate_token(id: int) -> str:
    now = datetime.now()
    token_limit = timedelta(days=14)
    token_expire_date = (now + token_limit).strftime('%Y%m%d%H%M')

    # id.expire-date
    payload = str(id) + '.' + token_expire_date
    token = encrypt(payload, settings.SECRET_KEY)

    return token
