from django import forms


class Upload(forms.Form):
	title = forms.CharField(max_length=50)
	file = forms.ImageField()
