import random

class PC:
	name = "unnamed"
	#Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
	attributes = [8, 8, 8, 8, 8, 8]
	pcclass = "no-class"
	
	def status():

	def wrongformat(command):

	def defattributes(args):

		if args[0] == "random":
			attributes = [15, 14, 13, 12, 10, 8]
			random.shuffle(attributes)

		elif is_number(args[0]):
			if len(args) == 5:
				attributes = args
			else:
				return wrongformat("defattributes")
		else:
			for i range(args):	
