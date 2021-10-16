from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse

from django.views.generic import View

from utils.mixins import LoginRequiredMixin

# from user.models import *
# from music.models import *

class IndexView(View):
    
    def get(self, request):

        context = {}

        return render(request, 'music/index.html', context=context)

#     def post(self, request):
#         do = request.POST.get('do')

#         if do == 'add-cart':
#             pizza = Pizza.objects.get(id=int(request.POST.get('pizza_id')))
#             user = request.user
#             Cart.objects.create(item=pizza, user=user, total=1)
#             res = True

#             return JsonResponse({'res': res}, status=200)

# class DetailView(View):
    
#     def get(self, request, pizza_id):
#         pizza = Pizza.objects.get(id=pizza_id)

#         context = {
#             'this_page': 'detail',
#             'pizza': pizza,
#         }

#         return render(request, 'pizza/detail.html', context=context)

#     def post(self, request, pizza_id):
#         user = request.user
#         pizza = Pizza.objects.get(id=int(request.POST.get('pizza_id')))
#         cart_total = int(request.POST.get('cart_total'))
#         do = request.POST.get('do')

#         if do == 'add-cart':
#             Cart.objects.create(item=pizza, user=user, total=cart_total)
#             res = True

#             return JsonResponse({'res': res}, status=200)
        
#         if do == 'buy':
#             Cart.objects.create(item=pizza, user=user, total=cart_total, status=1)
#             res = True

#             return JsonResponse({'res': res}, status=200)
    

class SearchView(View):
    def get(self, request):
        # search_text = request.GET.get('search_text')
        
#         pizzas = []

#         if search_text and search_text != '':
#             pizzas = Pizza.objects.filter(name__icontains=search_text)

#         context = {
#             'this_page': 'search',
#             'search_text': search_text,
#             'pizzas': pizzas,
#         }

        return render(request, 'music/search.html')


class LeaderboardView(View):
    def get(self, request):
        
        return render(request, 'music/leaderborad.html')
