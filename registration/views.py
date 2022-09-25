from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from .models import Users
from articles.views import index


def reg(request):
    return render(request, 'reg.html')


def create_account(request):
    user = Users.objects.filter(login=request.POST['login'])
    if user:
        return HttpResponse('Takoy polzovatel sushestvuet')
    else:
        u = Users(login=request.POST['login'], password=request.POST['password'])
        u.save()
        return HttpResponseRedirect(reverse('articles:index'))


def authorization(request):
    user = Users.objects.get(login=request.POST['login'], password=request.POST['password'])
    if user:
        return HttpResponseRedirect(reverse('articles:index'))
    else:
        return HttpResponse('Net yego!')
