from django import  forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout

from django.forms import fields
from .models import snippet

class contactForms(forms.Form):
    name=forms.CharField()
    email=forms.EmailField(label='E-mail')
    subject=forms.ChoiceField( choices=[('question','Question'),('other','Other')])
    body=forms.CharField(widget=forms.Textarea)

    def __init__(self,*args,**kargs):
        super().__init__(*args,kargs)
        self.helper.layout=Layout(
            'name',
            'email',
            'subject',
            'body',
            Submit('submit','Submit',css_class=('btn-succes'))
        )

class snippetForm(forms.ModelForm):
    class Meta:
        model=snippet
        fields=('name','body')