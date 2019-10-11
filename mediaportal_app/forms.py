from django import forms
from mediaportal_app.models import Article


class CommentCreationForm(forms.ModelForm):
	content = forms.CharField(widget=forms.Textarea, label='Comment')

	class Meta:
		model = Article
		fields = ['content']

	def __init__(self, *args, **kwargs):
		super(CommentCreationForm, self).__init__(*args, **kwargs)
