from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.contrib.auth.hashers import check_password, make_password

from fm_studio import settings

from user.models import User
from utils.auth import generate_token, verify_token
from utils.data import verify_data, get_data


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
            verify_data(password, min_length=4, max_length=64, data_type=str,
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

            return JsonResponse({'message': 'авторизация сәтті болды',
                                 'token': token,
                                 'user': user_obj
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
            verify_data(password, min_length=4, max_length=64, data_type=str,
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
            token_correct, response = verify_token(request)

            if token_correct and response.get('data').get('user').get('is_admin'):
                new_user = User.objects.create(
                    phone=phone, password=make_password(password, settings.SECRET_KEY), is_admin=is_admin)
            else:
                return JsonResponse({'message': 'админды құру үшін админ болу керек'}, status=401)
        else:
            new_user = User.objects.create(
                phone=phone, password=make_password(password, settings.SECRET_KEY))

        token = generate_token(new_user.id)
        user_obj = {
            'id': new_user.id,
            'username': new_user.username,
            'phone': new_user.phone,
            'is_admin': new_user.is_admin,
            'birthday': new_user.birthday,
            'gender': new_user.gender,
            'avatar': request.META.get('SERVER_PROTOCOL')[:request.META.get('SERVER_PROTOCOL').find('/')].lower()  + '://' + request.META.get('HTTP_HOST') + settings.MEDIA_URL + str(new_user.avatar),
            'create_time': new_user.create_time
        }

        return JsonResponse({'message': 'тіркелу сәтті болды',
                             'token': token,
                             'user': user_obj
                             }, status=201)


class EditView(View):

    def put(self, request):

        is_valid, response_context = verify_token(request)

        if not is_valid:
            return JsonResponse({'message': 'авторизация сәтсіз болды'}, stastus=401)

        user_current_info = response_context.get('data').get('user_attr')
        user = response_context.get('data').get('user')

        data = get_data(request)
        username = data.get("username")
        phone = data.get("phone")
        birthday = data.get("birthday")
        gender = data.get("gender")
        password = data.get("password")

        verify_list = [
            verify_data(phone, required=False, min_length=11, max_length=11, data_type=str,
                        error_messages={'required': 'телефон нөмер болу керек',
                                        'min_length': 'телефон нөмер 11 орынды болу керек',
                                        'max_length': 'телефон нөмер 11 орынды болу керек',
                                        'data_type': 'телефон нөмер string типынде болу керек'
                                        }),
            verify_data(password, required=False, min_length=4, max_length=64, data_type=str,
                        error_messages={'required': 'құпия сөз болу керек',
                                        'min_length': 'құпия сөз 4 орыннан аз болмау керек',
                                        'max_length': 'құпия сөз 64 орыннан көп болмау керек',
                                        'data_type': 'құпия сөз string типынде болу керек'
                                        }),
            verify_data(username, required=False, min_length=3, max_length=64, data_type=str,
                        error_messages={'min_length': 'атау 3 орыннан аз болмау керек',
                                        'max_length': 'атау 64 орыннан көп болмау керек',
                                        'data_type': 'атау string типынде болу керек'
                                        }),
            verify_data(birthday, required=False, min_length=10, max_length=10, data_type=str,
                        error_messages={'min_length': 'туылған күн форматы YYYY-MM-DD болу керек',
                                        'max_length': 'туылған күн форматы YYYY-MM-DD болу керек',
                                        'data_type': 'туылған күн форматы YYYY-MM-DD болу керек'
                                        }),

        ]

        for is_valid, error_message in verify_list:
            if not is_valid:
                return JsonResponse({'message': error_message}, status=400)

        if gender is not None and not isinstance(gender, bool):
            return JsonResponse({'message': "жыныс boolean типінде болу керек"}, status=400)

        user.username = username or user_current_info.get('username')
        user.phone = phone or user_current_info.get('phone')
        user.password = make_password(
            password, settings.SECRET_KEY) or user.password
        user.gender = gender or user_current_info.get('gender')
        user.birthday = birthday or user_current_info.get('birthday')
        user.save()

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

        return JsonResponse({'message': 'Өзгерту сәтті болд',
                             'user': user_obj
                             }, status=200)
