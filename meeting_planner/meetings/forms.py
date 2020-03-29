from django.forms import ModelForm
from django.forms.widgets import DateInput, TextInput, TimeInput
from django.core.exceptions import ValidationError
from meetings.models import Meeting
from _datetime import date


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={"type": "date"}),
            'start_time': TimeInput(attrs={"type": "time"}),
            'duration': TextInput(attrs={"type": "number", "min": "1", "max": "4"})
        }

    def clean_date(self):
        meeting_date = self.cleaned_data.get("date")
        if meeting_date < date.today():
            raise ValidationError("Meetings cannot be in the past")
        return meeting_date
