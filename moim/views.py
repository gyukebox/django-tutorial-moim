from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from moim.forms import MoimForm
from moim.models import MoimModel


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
        return render(request, template_name='moim-create.html', context={'form': form})

    def post(self, request):
        form = MoimForm(request.POST)
        if form.is_valid() is False:
            return HttpResponse(render(request, template_name='moim-create.html', context={'form': form}), status=400)
        # TODO save moim model
        return HttpResponse('Not Implemented!')


class MoimDetailView(View):
    def get(self, request, moim_id):
        moim_model = MoimModel.objects.get(id=moim_id)
        moim_detail = {
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
        return render(request, template_name='moim-detail.html', context=moim_detail)

    def put(self, request):
        return HttpResponse('Not Implemented!')

    def delete(self, request):
        return HttpResponse('Not Implemented!')
