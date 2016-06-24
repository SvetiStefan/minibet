from django.shortcuts import render
from initialise.models import User, Bandit
import datetime
# Create your views here.

def clear_inactive_user(request):
	ref_date = datetime.datetime.today() + datetime.timedelta(days=-6)
	users = User.objects.filter(updated__lte=ref_date)
	cnt = len(users)
	users.delete()
	return render(request, "clear.html", {"count":cnt})