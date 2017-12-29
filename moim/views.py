from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from moim.models import MoimModel


class IndexView(View):
    def get(self, request):
        opened_meetups_models = MoimModel.objects.all().order_by('-id')[:9]
        num_meetups = len(opened_meetups_models)
        opened_meetups = {
            'meetups': list()
        }

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
            opened_meetups['meetups'].append(row)

        return render(request, template_name="index.html", context=opened_meetups)


class MoimView(View):
    def get(self, request):
        return HttpResponse('Not Implemented!')

    def post(self, request):
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
        print(moim_detail)
        return render(request, template_name='moim-detail.html', context=moim_detail)

    def put(self, request):
        return HttpResponse('Not Implemented!')

    def delete(self, request):
        return HttpResponse('Not Implemented!')
