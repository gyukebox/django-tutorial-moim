from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from user.forms import LoginForm, RegisterForm
from user.models import UserModel


class UserLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, template_name='login.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid() is False:
            return HttpResponse(render(request, 'login.html', {'form': form}), status=400)
        else:
            input_data = form.cleaned_data
            try:
                UserModel.objects.filter(email=input_data['email']).filter(
                    password=input_data['password']).get()
            except (UserModel.DoesNotExist, UserModel.MultipleObjectsReturned):
                return HttpResponse(render(request, 'login.html', {'form': form}), status=400)

            return HttpResponseRedirect('/')


class UserRegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, template_name='register.html', context={'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid() is False:
            return HttpResponse(render(request, template_name='register.html', context={'form': form}), status=400)
        return HttpResponse('Not Implemented!')
