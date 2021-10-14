# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.http import HttpResponse, JsonResponse

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.hashers import check_password, make_password

# from django.views.generic import View


# from utils.mixin import LoginRequiredMixin

# from user.models import *
# from pizza.models import *


# class LoginView(View):
#     def get(self, request):
#         context = {
#             'this_page': 'log',
#         }

#         return render(request, 'user/log.html', context=context)

#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user is not None:
#             login(request, user)

#             next_url = request.GET.get('next', reverse('pizza:index'))
#             response = redirect(next_url)

#             return response
#         else:
#             return render(request, 'user/log.html', {'errmsg': 'Неверное имя пользователя или пароль!'})


# class RegisterView(View):
#     def get(self, request):
#         context = {
#             'this_page': 'reg',
#         }

#         return render(request, 'user/reg.html', context=context)

#     def post(self, request):
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             user = None

#         if user:
#             return render(request, 'user/reg.html', {'errmsg': 'Имя пользователя уже существует!'})

#         user = User.objects.create_user(username, password)
#         user.password = make_password(password)
#         user.save()

#         return redirect(reverse('user:log'))


# class LogoutView(View):
#     def get(self, request):
#         logout(request)

#         return redirect(reverse('pizza:index'))


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
