from django.http import JsonResponse
from django.views.generic import View

from user.models import *
from music.models import *

from utils.auth import verify_token
from utils.data import get_data, verify_data
from utils.model_attr import get_music_attr, get_music_type_attr


class MusicView(View):

    def post(self, request):

        is_valid, response_context = verify_token(request)
        if not is_valid:
            return JsonResponse(response_context, status=401)

        user = response_context.get('user')

        data = get_data(request)
        name = data.get('name')
        music_type = data.get('music_type')

        verify_list = [
            verify_data(name, min_length=1, max_length=40, data_type=str,
                        error_messages={'required': 'музыка атауы болу керек',
                                        'min_length': 'музыка атауы кем дегенде 1 орынды болу керек',
                                        'max_length': 'музыка атауы 40 орыннан аспау керек',
                                        'data_type': 'музыка атауы string типынде болу керек'
                                        }),
            verify_data(music_type, data_type=int,
                        error_messages={'required': 'музыка жанры болу керек',
                                        'data_type': 'музыка жанры int типынде болу керек'
                                        })]

        for is_valid, error_message in verify_list:
            if not is_valid:
                return JsonResponse({'message': error_message}, status=400)

        music = request.FILES.get('music')
        if music is None:
            return JsonResponse({'message': 'аудио болу керек'}, status=400)

        print('\nmusic size: ', music.size, '\n')
        # if music.size >= 500000:
        #     return JsonResponse({'message': 'аудио пішіні 60kb-дан артық болмау керек'}, status=400)

        try:
            music_type = MusicType.objects.get(id=music_type)
        except MusicType.DoesNotExist:
            return JsonResponse({'message': 'музыка жанры табылмады'}, status=400)

        # new_music = Music.objects.create(name=name, music=music, author=user)
        # new_music.music_type.add(music_type)

        # music_attr = get_music_attr(request, new_music)

        return JsonResponse({'message': 'музыка сәтті жүктелді',
                            #  'music': music_attr},
                             },
                            status=201)


class MusicTypeView(View):
    def get(self, request):
        all_music_types = MusicType.objects.all()
        all_music_types_attr = [get_music_type_attr(
            request, music_type) for music_type in all_music_types]

        return JsonResponse({'message': 'барлық жанрлар', 'data': all_music_types_attr}, status=200)

    def post(self, request):

        is_valid, response_context = verify_token(request)
        if not is_valid:
            return JsonResponse(response_context, status=401)

        user = response_context.get('user')
        if user.is_admin == False:
            return JsonResponse({'message': 'жанырды тек админ құруға болады'}, status=401)

        data = get_data(request)
        name = data.get('name')

        is_valid, error_message = verify_data(name, min_length=1, max_length=24, data_type=str,
                                              error_messages={'required': 'жаныр атауы болу керек',
                                                              'min_length': 'жаныр атауы кем дегенде 1 орынды болу керек',
                                                              'max_length': 'жаныр атауы 24 орыннан аспау керек',
                                                              'data_type': 'жаныр атауы string типынде болу керек'
                                                              })
        if is_valid is False:
            return JsonResponse({'message': error_message}, status=400)

        try:
            music_type = MusicType.objects.get(name=name)
        except MusicType.DoesNotExist:
            music_type = None

        if music_type:
            return JsonResponse({'message': 'жанр құрылған'}, status=400)

        new_music_type = MusicType.objects.create(name=name)
        music_type_attr = get_music_type_attr(request, new_music_type)

        return JsonResponse({'message': 'музыка жаныры сәтті құрылды',
                             'music': music_type_attr}, status=201)
