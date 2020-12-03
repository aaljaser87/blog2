from django import forms
from .models import *

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text', 'author')


# class Post(forms.Form):
# 	CHOICES = (('1', 'arwa'), ('2', 'ahmed'))
# 	title = forms.CharField(max_length=200)
# 	text = forms.TextField()
# 	author = forms.ChoiceField(choices=CHOICES)
# 	mobile= forms.CharField()