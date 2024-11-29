from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Portfolio, PortfolioFile

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class PortfolioForm(forms.ModelForm):
    portfolios = MultipleFileField(required=False, label=_("Portfolios"))

    class Meta:
        model = Portfolio
        fields = ['name', 'profession', 'avatar', 'figma', 'telegram', 'description']

class PortfolioFileForm(forms.ModelForm):
    class Meta:
        model = PortfolioFile
        fields = ['file']