from django.db.utils import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from moim.forms import MoimForm
from moim.models import MoimModel
from user.models import UserModel


class IndexView(View):
    def get(self, request, page_num=1):
        context = dict()

        if 'logged-in' in request.session:
            if request.session['logged-in'] is True:
                context['current_user'] = request.session['logged-in-user']
        else:
            request.session['logged-in'] = False
            request.session['logged-in-user'] = None

        context['meetups'] = list()

        if 'total-meetups' not in request.session:
            request.session['total-meetups'] = len(MoimModel.objects.all())

        opened_meetups_models = MoimModel.objects.all().order_by(
            '-id')[(page_num - 1) * 9:page_num * 9]
        num_meetups = len(opened_meetups_models)

        for i in range(3):
            row = list()
            for j in range(3):
                index = 3 * i + j
                if index >= num_meetups:
                    break
                meetup_info = {
                    'id': opened_meetups_models[index].id,
                    'name': opened_meetups_models[index].title,
                    'about': opened_meetups_models[index].summary,
                    'image_path': str(opened_meetups_models[index].image)
                }
                row.append(meetup_info)
            context['meetups'].append(row)

        if page_num > 1:
            context['previous'] = page_num - 1
        if page_num * 9 < request.session['total-meetups']:
            context['next'] = page_num + 1

        return render(request, template_name="index.html", context=context)


class MoimView(View):
    def get(self, request):
        if 'logged-in' not in request.session:
            return HttpResponseRedirect('/users/login')
        elif request.session['logged-in'] is False:
            return HttpResponseRedirect('/users/login')

        form = MoimForm()

        context = {
            'current_user': request.session['logged-in-user'],
            'form': form
        }

        return render(request, template_name='moim-create.html', context=context)

    def post(self, request):
        form = MoimForm(request.POST)

        context = {
            'current_user': request.session['logged-in-user'],
            'form': form
        }

        print(form.data)

        if form.is_valid() is False:
            return HttpResponse(render(request, template_name='moim-create.html', context=context), status=400)

        data = form.cleaned_data
        new_model = MoimModel(title=data['title'], starts_at=data['starts_at'], max_attendee=data['max_attendee'],
                          summary=data['summary'], description=data['description'], image=data['image'])
        new_model.creator = UserModel.objects.get(name=request.session['logged-in-user'])

        try:
            new_model.save()
        except IntegrityError:
            return HttpResponse(render(request, template_name='moim-create.html', context=context), status=400)

        return HttpResponseRedirect('/moim/{}'.format(new_model.id), status=201)


class MoimDetailView(View):
    def get(self, request, moim_id):
        moim_model = MoimModel.objects.get(id=moim_id)
        context = {
            'id': moim_model.id,
            'title': moim_model.title,
            'created_by': moim_model.creator.name,
            'starts_at': moim_model.starts_at,
            'max_attendee': moim_model.max_attendee,
            'attendees': [person.name for person in moim_model.attendees.all()],
            'summary': moim_model.summary,
            'description': moim_model.description,
            'image_path': str(moim_model.image)
        }

        if 'logged-in' in request.session:
            if request.session['logged-in'] is True:
                context['current_user'] = request.session['logged-in-user']

        return render(request, template_name='moim-detail.html', context=context)

    def put(self, request):
        return HttpResponse('Not Implemented!')

    def delete(self, request):
        return HttpResponse('Not Implemented!')


class MoimApplyView(View):
    def get(self, request, moim_id):
        if 'logged-in' not in request.session:
            return HttpResponseRedirect('/user/login')
        elif request.session['logged-in'] is False:
            return HttpResponseRedirect('/user/login')

        moim = MoimModel.objects.get(id=moim_id)
        print(moim)
        user = UserModel.objects.get(name=request.session['logged-in-user'])
        print(user)

        if len(moim.attendees.all()) == moim.max_attendee - 1:
            return HttpResponseRedirect('/', status=400)
        else:
            moim.attendees.add(user)
            moim.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
