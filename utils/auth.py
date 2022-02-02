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

            return True, {'message': 'авторизация сәтті болды', 'user': user}
        else:
            return False, {'message': 'авторизация мерзімі аяқталды'}

    return False, {'message': 'авторизация сәтсіз болды'}


def generate_token(id: int) -> str:
    now = datetime.now()
    token_limit = timedelta(days=14)
    token_expire_date = (now + token_limit).strftime('%Y%m%d%H%M')

    # id.expire-date
    payload = str(id) + '.' + token_expire_date
    token = encrypt(payload, settings.SECRET_KEY)

    return token
