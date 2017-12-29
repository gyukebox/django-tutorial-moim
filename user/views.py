from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import RedirectView, TemplateView
from user.models import UserModel


class UserLoginView(View):
    def post(self):
        return HttpResponse('Not Implemented!')


class UserRegisterView(View):
    def post(self):
        return HttpResponse('Not Implemented!')
