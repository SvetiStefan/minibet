from django.contrib import admin
from .models import Bandit
from .forms import BanditForm

# Register your models here.
class BanditAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "p", "reward"]
	form = BanditForm

admin.site.register(Bandit, BanditAdmin)