from django import forms
from django.conf import settings
import requests

class BasicSearchForm(forms.Form):
    object_id = forms.CharField()

    def get_catalog(self):
        object_id = self.cleaned_data.get('object_id')
        response = requests.get(settings.BK_API_URL_TEMPLATE.format(
            OBJECT_ID=object_id,
            API_KEY=settings.BK_API_KEY
        )).json()
        return response.get('response', {})
