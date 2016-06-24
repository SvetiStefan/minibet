from django.shortcuts import render
from .models import User
import uuid
import random

# Create your views here.
def home(request):
	return render(request, "home.html", {})

def gen_order():
	l = list(range(1,6))
	random.shuffle(l)
	order = 0
	for i in l:
		order = order*10 + i
	return order

def inigame(request):
	uid = str(uuid.uuid4()).replace('-','')[:4].lower()
	while User.objects.filter(uid=uid).exists():
		uid = str(uuid.uuid4()).replace('-','')[:4].lower()
	order = gen_order()
	new_user = User(uid=uid, balance=200.0, order=order)
	new_user.save()
	context = {"username":uid, "balance":200, "order":order}
	return render(request, "inigame.html", context)
