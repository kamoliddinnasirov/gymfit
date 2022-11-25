from django import forms
from contact.models import ContactSendModel


# class ContactSendForm(forms.ModelForm):
#     class Meta:
#         model = ContactSendModel
#         exclude = ['title', 'sub_title', 'created_at']


class ContactSendForm(forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    phone = forms.CharField(max_length=13)
    message = forms.CharField(widget=forms.Textarea, help_text="Message...")
