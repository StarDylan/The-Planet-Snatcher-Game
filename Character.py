
class character:

	def __init__(self, strength, mind, food, agility, water):
		self.strength = strength
		self.mind = wisdom
		self.food = food
		self.agility = agility
		self.water = water

		def addStrength():
			self.strength++
		def removeStrength():
			self.Strength--
		def addMind():
			self.mind++
		def removeMind():
			self.mind--
		def addFood():
			self.food++
		def removeFood():
			self.food--
		def addAgility():
			self.agility++
		def removeAgility():
			self.agility--
		def addWater():
			self.water++
		def removeWater():
			self.water--

	def do_attack(self,amount):
		import random
		atkv = random.randint(1,50)
		if atkv in range(1,24):
				atk == 1
		if atkv in range(25,self.strength):
				atk == 1
		if atkv in range(int(self.strength + 1), 51):
				atk == 0
