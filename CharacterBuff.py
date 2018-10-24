
class character:

	def __init__(self, strength, wisdom, hunger, clever, thirst):
		self.strength = strength
		self.wisdom = wisdom
		self.hunger = hunger
		self.clever = clever
		self.thirst = thirst

	def addStrength(self):
		self.strength = int(self.strength + 1)

	def addWisdom(self):
		self.wisdom = int(self.wisdom + 1)

	def addHunger(self):
		self.hunger = int(self.hunger + 1)

	def minHunger(self):
		self.hunger = int(self.hunger - 1)

	def addCleverness(self):
		self.clever = int(self.clever + .2)

	def drink(self):
		self.thirst = int(self.thrist == 10)

	def thirsty(self):
		self.thirst = int(self.thrist - 1)

	def status(self):
		return 'Strength: {}, Wisdom: {}, Hunger: {}, Cleverness: {}'.format(self.strength, self.wisdom, self.hunger, self.clever)


	def do_attack(self,amount):
		import random
		atkv = random.randint(1,50)
		if atkv in range(1,24):
				atk == 1
		if atkv in range(25,self.strength):
				atk == 1
		if atkv in range(int(self.strength + 1), 51):
				atk == 0
