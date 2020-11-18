from django.db import models,migrations

# Create your models here.
class club(models.Model):
	name = models.CharField(max_length=220)
	money = models.IntegerField()
	def __str__(self):
		return self.name



    