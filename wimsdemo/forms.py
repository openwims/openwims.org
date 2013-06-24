from django import forms

class WimDemoForm(forms.Form):

    sentence = forms.CharField( min_length=3, widget=forms.Textarea(attrs={'rows':3}) )