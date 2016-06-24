from django.db import models

# Create your models here.
class Bandit(models.Model):
	id = models.IntegerField(primary_key=True)
	p = models.DecimalField(max_digits=3, decimal_places=2)
	reward = models.DecimalField(max_digits=3, decimal_places=1)
	
	def __unicode__(self):
		return str(self.id)

class User(models.Model):
	uid = models.CharField(max_length=4, primary_key=True)
	order = models.IntegerField(default=54321)
	balance = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	def __unicode__(self):
		return self.uid