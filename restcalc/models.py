from django.db import models
from restcalc.calc import Calc

class Calculation(models.Model):
	owner = models.ForeignKey('auth.User', related_name='calculation')
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=30, blank=True, default='')
	calculation = models.TextField()
	value = models.TextField(blank=True, default='')

	class Meta:
	    ordering = ('created',)

	def save(self, *args, **kwargs):
			o = Calc(self.calculation)
			self.value = o.doCalc()
			super(Calculation, self).save(*args, **kwargs)