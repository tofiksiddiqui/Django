from django import forms

class StudentForm(forms.Form):
	ID = forms.IntegerField()
	name = forms.CharField()
	address = forms.CharField(widget = forms.TextInput(attrs={'class':'Address','ID':'Uniqueid'}))
	contact = forms.IntegerField()
	email = forms.EmailField()
	passwd = forms.CharField(widget = forms.PasswordInput())
	comment = forms.CharField()
	Text_Area = forms.CharField(widget = forms.Textarea())
	file = forms.CharField(widget = forms.FileInput())
	select = forms.CharField(widget = forms.CheckboxInput())