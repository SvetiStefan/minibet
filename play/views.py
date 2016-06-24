from django.shortcuts import render
from initialise.models import User, Bandit
import random



def get_game(order, game_id):
	real_game_id = ((order / pow(10, game_id - 1)) % 10)
	game = Bandit.objects.get(id=real_game_id)
	return game.p, game.reward

# Create your views here.
def playgame(request):
	items = request.path.split('/')
	uid = items[1]
	game_id = int(items[2])
	content = ''
	if game_id < 1 or game_id > 5:
		content = "Invalid game id. Game id should be in [1,5]."
	elif not User.objects.filter(uid=uid).exists():
		content = "Invalid user name."
	else:
		user = User.objects.get(uid=uid)
		if user.balance < 0:
			content = "Sorry, you lost all your money. Game over!"
		elif user.balance >= 1000:
			content = "You win too much money. We have gone bankrupt! Game over!"
		else:
			content = "You bet on game {0} with $1. ".format(game_id)
			p, reward = get_game(user.order, game_id)
			win = True if random.random() < p else False
			if win:
				user.balance += float(reward)
				content += "Congrats! You win ${0}. Your current balance is ${1}.".format((reward+1), user.balance)
			else:
				user.balance -= 1
				content += "Ooops you lose. Your current balance is ${0}.".format(user.balance)
			user.save()
			if user.balance < 0:
				content += "Sorry, you lost all your money. Game over!"
			elif user.balance >= 1000:
				content += "You win too much money. We have gone bankrupt! Game over!"

	return render(request, "playgame.html", {"message":content})