from django import forms
from .models import Bandit

class BanditForm(forms.ModelForm):
	class Meta:
		model = Bandit
		fields = ['id', 'p', 'reward']