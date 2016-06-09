import requests
import re

class Calc:
	
	def __init__(self, expression):
		self.expression = expression

	def doCalc(self):
		"""
		TODO
		Lets see if we can figure out a way to access other things in the database
		from here so that we can use them as 'memory variables'
		"""
		#resp = requests.get('http://localhost:8000/snippets/?page=7')
		# get list of items in database
		# IT'S CURRENTLY NOT GETTING ALL THE DATABASE ENTRIES!!
		resp = requests.get('http://localhost:8000/snippets/')
		if resp.status_code != 200:
		    # This means something went wrong.
		    raise ApiError('GET /snippets/ {}'.format(resp.status_code))

		#for text in self.expression:
		wordList = re.findall(r"\b[a-zA-Z]+\b", self.expression) # find text in expression
		if wordList: # look for text in json
			print wordList
			# For every item in results, search for memvar name we're looking for
			for word in wordList:
				for item in resp.json()["results"]:
					print item["title"] + " vs. " + word
					if item["title"] == word:
						print(item["code"])
						# replace text with json value
						reg = r"\b" + word + r"\b"
						self.expression = re.sub(reg, item["code"], self.expression)

		return str(eval(self.expression))
#		return self.expression
