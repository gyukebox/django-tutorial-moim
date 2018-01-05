from django import forms
from django.utils import timezone


class MoimForm(forms.Form):
    title = forms.CharField(max_length=20, label='모임의 제목')
    starts_at = forms.DateTimeField(
        error_messages={'past': '시작 시간은 지금 시간보다 빠를 수 없습니다!', })
    max_attendee = forms.IntegerField(min_value=1)
    summary = forms.CharField(min_length=1, max_length=100, label='한줄 요약')
    description = forms.CharField(
        min_length=1, widget=forms.Textarea, label='상세 설명')
    image = forms.FileField(label='모임을 잘 설명할 수 있는 이미지!', required=False)

    def is_valid(self):
        if super(MoimForm, self).is_valid() is False:
            return False
        else:
            data = self.cleaned_data
            if data['starts_at'] <= timezone.now():
                return False
            else:
                return True
