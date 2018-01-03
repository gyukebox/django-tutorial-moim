from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from moim.models import MoimModel


class MoimForm(forms.ModelForm):
    class Meta:
        model = MoimModel
        exclude = ['creator', 'attendees']
        labels = {
            'title': '모임의 제목',
            'starts_at': '모임의 시작 시간',
            'max_attendee': '정원',
            'summary': '한줄요약',
            'description': '상세 설명',
            'image': '모임을 잘 설명할 수 있는 이미지!'
        }
        widgets = {
            'starts_at': forms.SelectDateWidget(),
        }
