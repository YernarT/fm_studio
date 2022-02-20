from django.core.handlers.wsgi import WSGIRequest
from fm_studio import settings

from user.models import User
from music.models import Music, MusicType


def get_media_url(request: WSGIRequest, resource_url: str) -> str:
    '''get the full path of the media resource'''

    server_protocol = request.META.get('SERVER_PROTOCOL')[
        :request.META.get('SERVER_PROTOCOL').find('/')
    ].lower()
    host = request.META.get('HTTP_HOST')

    return server_protocol + '://' + host + settings.MEDIA_URL + str(resource_url)


def get_user_attr(request: WSGIRequest, user_obj: User) -> dict:
    '''user attributes for response'''
    from datetime import datetime

    return {
        'username': user_obj.username,
        'phone': user_obj.phone,
        'is_admin': user_obj.is_admin,
        'birthday': datetime.strftime(user_obj.birthday, '%Y-%m-%d') if user_obj.birthday else None,
        'gender': user_obj.gender,
        'avatar': get_media_url(request, user_obj.avatar),
        'create_time': datetime.strftime(user_obj.create_time, '%Y-%m-%d %H:%M:%S')
    }


def get_music_attr(request: WSGIRequest, music_obj: Music) -> dict:
    '''music attributes for response'''
    from datetime import datetime

    print('\n\n musciType: ', music_obj.music_type, '\n\n')

    return {
        'id': music_obj.id,
        'name': music_obj.name,
        'music_type': str(music_obj.music_type),
        'author': music_obj.author.id,
        'views': music_obj.views,
        'music': get_media_url(request, music_obj.music),
        'create_time': datetime.strftime(music_obj.create_time, '%Y-%m-%d %H:%M:%S')
    }


def get_music_type_attr(request: WSGIRequest, music_type_obj: MusicType) -> dict:
    '''music type attributes for response'''

    return {
        'id': music_type_obj.id,
        'name': music_type_obj.name
    }
