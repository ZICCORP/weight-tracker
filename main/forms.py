from django.forms import ModelForm
from main.models import BodyWeight


class BodyWeightForm(ModelForm):
    class Meta:
        model = BodyWeight
        fields = ['weight',]