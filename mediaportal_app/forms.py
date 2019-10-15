from django import forms
from mediaportal_app.models import Article
from django.contrib.auth.models import User


class CommentCreationForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea, label='Comment')

	class Meta:
		model = Article
		fields = ('content',)

	def __init__(self, *args, **kwargs):
		super(CommentCreationForm, self).__init__(*args, **kwargs)


class RegistrationForm(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	password_check = forms.CharField(widget=forms.PasswordInput, label='Repeat password')
	email = forms.CharField(widget=forms.EmailInput, help_text='Please, provide real email address')

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password', )

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
	
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		password_check = self.cleaned_data.get('password_check')
		email = self.cleaned_data.get('email')
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("User with this username already exists.")
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("User with this email already exists.")
		if password != password_check:
			raise forms.ValidationError("Passwords dont match.")