import random

class PC:
	name = "unnamed"
	#Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
	attributes = [8, 8, 8, 8, 8, 8]
	possibleclasses = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Ranger", "Rogue", "Sorceror", "Warlock", "Wizard"]
	pcclass = "no-class"
	possibleraces = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-elf", "Half-orc", "Human"]
	pcrace = "no-race"
	
	def status():
		return "OK"

	def wrongformat(command):
		return "WRONG"

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
			if len(args) % 2 != 0:
				return wrongformat("defattributes")
			for i range(len(args)/2):
				if args[i*2] == "str":
					idx = 0
				elif args[i*2] == "dex":
					idx = 1
				elif args[i*2] == "con":
					idx = 2
				elif args[i*2] == "int":
					idx = 3
				elif args[i*2] == "wis":
					idx = 4
				elif args[i*2] == "cha":
					idx = 5
				else:
					return wrongformat("defattributes")
				attributes[idx] = args[i*2+1]

		return status()		

	def defclass(args):
		if args[0] in possibleclasses:
			pcclass = args[0]
			return status()
		else:
			return wrongformat("defclass")

	def defrace(args):
		if args[0] in possibleraces:
			pcrace = args[0]
			return status()
		else:
			return wrongformat("defclass")
