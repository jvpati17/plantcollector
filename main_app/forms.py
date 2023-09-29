from django.forms import ModelForm
from .models import Watered, Status

class WateredForm(ModelForm):
    class Meta:
        model = Watered
        fields = ['date', 'fed']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['date', 'no_of_leaves', 'state', 'status_log']