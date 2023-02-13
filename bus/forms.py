from django.forms import ModelForm
from .models import TimeAssignModel
from django.core.exceptions import ValidationError


class TimeAssignModelForm(ModelForm):
    is_cleaned =True
    class Meta:
        model = TimeAssignModel
        fields = ['bus', 'route', 'from_time', 'to_time']
