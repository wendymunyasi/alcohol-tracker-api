from django import forms

class NewsLetterForm(forms.Form):
    email = forms.EmailField(label='Email')
