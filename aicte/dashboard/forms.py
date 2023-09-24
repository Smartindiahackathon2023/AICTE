from django.forms import ModelForm
from .models import Curriculumn


class CurriculumnForm(ModelForm):
    class Meta:
        model=Curriculumn
        fields=['body']