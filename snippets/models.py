from django.db import models
from pygments import highlight
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments.styles import get_all_styles
from snippets.calc import Calc

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Snippet(models.Model):
	owner = models.ForeignKey('auth.User', related_name='snippets')
	highlighted = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	code = models.TextField()
	linenos = models.BooleanField(default=False)
	language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
	style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
	
	class Meta:
		ordering = ('created',)

	def save(self, *args, **kwargs):
		"""
		Instead of doing an eval here, we could do a function something like "doCalc"
		that would be in a different file, get the 'code/payload' and replace any
		mem variables with the appropriate value and then eval the calculation
		"""
		#self.title = str(eval(self.code))
		o = Calc(self.code)
		self.code = o.doCalc()

		"""
		Use the `pygments` library to create a highlighted HTML
		representation of the code snippet.
		"""
		lexer = get_lexer_by_name(self.language)
		linenos = self.linenos and 'table' or False
		options = self.title and {'title': self.title} or {}
		formatter = HtmlFormatter(style=self.style, linenos=linenos,
		                          full=True, **options)
		self.highlighted = highlight(self.code, lexer, formatter)
		super(Snippet, self).save(*args, **kwargs)