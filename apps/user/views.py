from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.hashers import check_password, make_password

from fm_studio import settings

from .models import User
from utils.auth import generate_token, verify_token
from utils.data import verify_data, get_data, get_user_attr





class LoginView(View):

    def post(self, request):
        data = get_data(request)
        phone = data.get('phone')
        password = data.get('password')

        verify_list = [
            verify_data(phone, min_length=11, max_length=11, data_type=str,
                        error_messages={'required': 'телефон нөмер болу керек',
                                        'min_length': 'телефон нөмер 11 орынды болу керек',
                                        'max_length': 'телефон нөмер 11 орынды болу керек',
                                        'data_type': 'телефон нөмер string типынде болу керек'
                                        }),
            verify_data(password, min_length=4, max_length=60, data_type=str,
                        error_messages={'required': 'құпия сөз болу керек',
                                        'min_length': 'құпия сөз 4 орыннан аз болмау керек',
                                        'max_length': 'құпия сөз 64 орыннан көп болмау керек',
                                        'data_type': 'құпия сөз string типынде болу керек'
                                        })]

        for is_valid, error_message in verify_list:
            if not is_valid:
                return JsonResponse({'message': error_message}, status=400)

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return JsonResponse({'message': 'авторизация сәтсіз болды'}, status=400)

        if check_password(password, user.password):
            token = generate_token(user.id)

            user_attr = get_user_attr(request, user)

            return JsonResponse({'message': 'авторизация сәтті болды',
                                 'token': token,
                                 'user': user_attr
                                 }, status=200)

        return JsonResponse({'message': 'авторизация сәтсіз болды'}, status=400)


class RegisterView(View):

    def post(self, request):
        data = get_data(request)
        phone = data.get('phone')
        password = data.get('password')
        is_admin = data.get('is_admin')

        verify_list = [
            verify_data(phone, min_length=11, max_length=11, data_type=str,
                        error_messages={'required': 'телефон нөмер болу керек',
                                        'min_length': 'телефон нөмер 11 орынды болу керек',
                                        'max_length': 'телефон нөмер 11 орынды болу керек',
                                        'data_type': 'телефон нөмер string типынде болу керек'
                                        }),
            verify_data(password, min_length=4, max_length=60, data_type=str,
                        error_messages={'required': 'құпия сөз болу керек',
                                        'min_length': 'құпия сөз 4 орыннан аз болмау керек',
                                        'max_length': 'құпия сөз 64 орыннан көп болмау керек',
                                        'data_type': 'құпия сөз string типынде болу керек'
                                        })]

        for is_valid, error_message in verify_list:
            if not is_valid:
                return JsonResponse({'message': error_message}, status=400)

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            user = None

        if user:
            return JsonResponse({'message': 'телефон нөмер тіркелген'}, status=400)

        # to create admin
        if is_admin:
            is_valid, error_message = verify_data(is_admin, data_type=bool, required=False,
                                                  error_messages={'data_type': 'is_admin өрісі bool тиынде болу керек'})

            if not is_valid:
                return JsonResponse({'message': error_message}, status=400)

            # check request.user(request originator) is admin
            token_correct, response_context = verify_token(request)

            if token_correct and response_context.get('user').get('is_admin'):
                new_user = User.objects.create(
                    phone=phone, password=make_password(password, settings.SECRET_KEY), is_admin=is_admin)
            else:
                return JsonResponse({'message': 'админды құру үшін админ болу керек'}, status=401)
        else:
            new_user = User.objects.create(
                phone=phone, password=make_password(password, settings.SECRET_KEY))

        token = generate_token(new_user.id)
        user_attr = get_user_attr(request, new_user)

        return JsonResponse({'message': 'тіркелу сәтті болды',
                             'token': token,
                             'user': user_attr
                             }, status=201)


class EditView(View):

    def put(self, request):
        is_valid, response_context = verify_token(request)

        if not is_valid:
            return JsonResponse(response_context, status=401)

        user = response_context.get('user')
        user_attr = get_user_attr(request, user)

        data = get_data(request)
        username = data.get("username")
        phone = data.get("phone")
        password = data.get("password")
        birthday = data.get("birthday")
        gender = data.get("gender")

        verify_list = [
            verify_data(phone, required=False, min_length=11, max_length=11, data_type=str,
                        error_messages={'required': 'телефон нөмер болу керек',
                                        'min_length': 'телефон нөмер 11 орынды болу керек',
                                        'max_length': 'телефон нөмер 11 орынды болу керек',
                                        'data_type': 'телефон нөмер string типынде болу керек'
                                        }),
            verify_data(username, required=False, min_length=2, max_length=24, data_type=str,
                        error_messages={'min_length': 'атау 2 орыннан аз болмау керек',
                                        'max_length': 'атау 24 орыннан көп болмау керек',
                                        'data_type': 'атау string типынде болу керек'
                                        }),
            verify_data(password, required=False, min_length=4, max_length=60, data_type=str,
                        error_messages={'required': 'құпия сөз болу керек',
                                        'min_length': 'құпия сөз 4 орыннан аз болмау керек',
                                        'max_length': 'құпия сөз 60 орыннан көп болмау керек',
                                        'data_type': 'құпия сөз string типынде болу керек'
                                        }),
            verify_data(birthday, required=False, min_length=10, max_length=10, data_type=str,
                        error_messages={'min_length': 'туылған күн форматы YYYY-MM-DD болу керек',
                                        'max_length': 'туылған күн форматы YYYY-MM-DD болу керек',
                                        'data_type': 'туылған күн форматы YYYY-MM-DD болу керек'
                                        }),
            verify_data(gender, required=False, data_type=bool,
                        error_messages={'data_type': 'жыныс boolean типінде болу керек'}),
        ]

        for is_valid, error_message in verify_list:
            if not is_valid:
                return JsonResponse({'message': error_message}, status=400)

        # exact check
        if phone and phone != user.phone:
            try:
                same_phone_user = User.objects.get(phone=phone)
            except User.DoesNotExist:
                same_phone_user = None

            if same_phone_user:
                return JsonResponse({'message': 'телефон нөмер тіркелген'}, status=400)

        if username:
            import re
            if re.search(r'\W', username) != None:
                return JsonResponse({'message': 'атауда таңбаларды қолдануға болмайды'}, status=400)

        if birthday:
            import re
            if re.search(r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$', birthday) == None:
                return JsonResponse({'message': 'туылған күн форматы YYYY-MM-DD болу керек'}, status=400)

            from datetime import datetime
            year = list(map(int, birthday.split('-')))[0]
            is_valid, error_message = verify_data(year, data_type=int, min=1940, max=datetime.now().year, error_messages={
                'min': 'туылған күннің жылы 1940 дан кейін болу керек',
                'max': f'туылған күннің жылы {datetime.now().year} дан бұрын болу керек'
            })

            if not is_valid:
                return JsonResponse({'message': error_message}, status=400)

            try:
                birthday = datetime.strptime(birthday, '%Y-%m-%d')
            except:
                return JsonResponse({'message': 'туылған күн дұрыс емес'}, status=400)

        # edit
        user.username = username or user.username
        user.phone = phone or user.phone
        user.password = make_password(
            password, settings.SECRET_KEY) if password else user.password
        user.gender = gender if gender is not None else user.gender
        user.birthday = birthday or user.birthday
        user.save()

        user_attr = get_user_attr(request, user)

        return JsonResponse({'message': 'өзгерту сәтті болд',
                             'user': user_attr
                             }, status=200)


class EditAvatarView(View):
    def post(self, request):
        is_valid, response_context = verify_token(request)

        if not is_valid:
            return JsonResponse(response_context, status=401)

        user = response_context.get('user')

        avatar = request.FILES.get('avatar')
        if avatar is None:
            return JsonResponse({'message': 'сурет форматты тек jpg, png, jpeg болу керек'}, status=400)

        if avatar.size >= 500000:
            return JsonResponse({'message': 'сурет пішіні 60kb-дан артық болмау керек'}, status=400)

        import re
        if not re.search('.*(jpg|png|jpeg)$', avatar.name):
            return JsonResponse({'messgae': 'сурет форматты тек jpg, png, jpeg болу керек'}, status=400)

        # delete previous avatar
        from os import remove
        if user.avatar != 'img/user/avatar/default-avatar.png':
            remove(settings.MEDIA_ROOT + '\\' +
                   str(user.avatar).replace('/', '\\'))

        user.avatar = avatar
        user.save()
        user_attr = get_user_attr(request, user)

        return JsonResponse({'message': 'өзгерту сәтті болд', 'user': user_attr}, status=201)
