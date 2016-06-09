import requests
import re

class Calc:
	
	def __init__(self, expression):
		self.expression = expression

	def doCalc(self):
		# get list of items in database
		resp = requests.get('http://localhost:8000/calculations/')
		if resp.status_code != 200:
		    # This means something went wrong.
		    raise ApiError('GET /calculations/ {}'.format(resp.status_code))

		"""
		TODO: Do some basic error checking
		"""
		wordList = re.findall(r"\b[a-zA-Z]+\b", self.expression) # find text in expression
		if wordList: # look for text in json
			#print wordList
			# For every item in results, search for memvar name we're looking for
			for word in wordList:
				for item in resp.json()["results"]:
					#print item["name"] + " vs. " + word
					if item["name"] == word:
						#print(item["value"])
						# replace text with json value
						reg = r"\b" + word + r"\b"
						self.expression = re.sub(reg, item["value"], self.expression)

		return str(eval(self.expression))
