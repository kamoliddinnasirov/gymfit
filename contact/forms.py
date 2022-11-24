from django import forms
from contact.models import ContactSendModel


class ContactSendForm(forms.ModelForm):
    class Meta:
        model = ContactSendModel
        exclude = ['title', 'sub_title', 'created_at']
