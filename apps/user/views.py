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
                return JsonResponse({'messgae': error_message}, status=400)

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            return JsonResponse({'messgae': 'авторизация сәтсіз болды'}, status=400)

        if check_password(password, user.password):
            token = generate_token(user.id)

            user_obj = {
                'id': user.id,
                'username': user.username,
                'phone': user.phone,
                'is_admin': user.is_admin,
                'birthday': user.birthday,
                'gender': user.gender,
                'avatar': request.get_host()+settings.MEDIA_URL+str(user.avatar),
                'create_time': user.create_time
            }

            return JsonResponse({'message': 'авторизация сәтті болды', 'data': {
                'token': token,
                'user': user_obj
            }}, status=200)

        return JsonResponse({'messgae': 'авторизация сәтсіз болды'}, status=400)


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
                return JsonResponse({'messgae': error_message}, status=400)

        try:
            user = User.objects.get(phone=phone)
        except User.DoesNotExist:
            user = None

        if user:
            return JsonResponse({'messgae': 'телефон нөмер тіркелген'}, status=400)

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
                return JsonResponse({'messgae': 'админды құру үшін админ болу керек'}, status=401)
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
            'avatar': request.get_host()+settings.MEDIA_URL+str(new_user.avatar),
            'create_time': new_user.create_time
        }

        return JsonResponse({'message': 'тіркелу сәтті болды', 'data': {
            'token': token,
            'user': user_obj
        }}, status=201)


# class UserInfoView(LoginRequiredMixin, View):
#     def get(self, request):
#         panel = request.GET.get('panel')

#         if panel != 'user_info' and panel != 'cart':
#             panel = 'user_info'

#         carts = Cart.objects.filter(user=request.user)

#         context = {
#             'this_page': 'user_info',
#             'panel': panel,
#             'carts': carts,
#         }

#         return render(request, 'user/user_info.html', context=context)

#     def post(self, request):
#         if 'change_info' in request.POST:
#             username = request.POST.get('username')
#             password = request.POST.get('new_password')

#             user = request.user

#             if (user.username == username):
#                 pass
#             else:
#                 try:
#                     other_user = User.objects.get(username=username)

#                     errmsg = 'Имя пользователя уже существует!'

#                     return render(request, 'user/user_info.html', {
#                         'this_page': 'user_info',
#                         'panel': 'user_info',
#                         'errmsg': errmsg,
#                     })
#                 except:
#                     user.username = username

#             if password != '':
#                 user.password = make_password(password)

#             return render(request, 'user/user_info.html', {
#                 'this_page': 'user_info',
#                 'panel': 'user_info',
#                 'backmsg': 'Успешно изменено!',
#             })

#         if 'del_cart' in request.POST:
#             cart = Cart.objects.get(id=int(request.POST.get('cart_id')))
#             cart.delete()

#             return JsonResponse({'res': True}, status=200)

#         if 'buy' in request.POST:
#             cart = Cart.objects.get(id=int(request.POST.get('cart_id')))
#             pizza = Pizza.objects.get(id=cart.item.id)

#             if cart.total <= pizza.total :
#                 result = True
#                 pizza.total -= 1
#                 pizza.save()

#                 cart.status = 1
#                 cart.save()
#             else:
#                 result = False

#             return JsonResponse({'res': result}, status=200)
