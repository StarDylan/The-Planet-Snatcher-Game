import os
import time
import sys
from pathlib import Path
import random
import CharacterBuff

attack = 0




character = buff(25, 25, 0, 25, 10)

#encounter defines



#turn system
def roll():
	for y in range(0,20):
		randomP()
		character.thirst()
		character.addhngr()
def randomP():
	clearScreen()
	import random
	x = random.randint(1,3)
	if x == 1:
		campsite()

	elif x == 2:
		creature_enc()

	elif x == 3:
		safespot()

	elif x == 4:
		anything()


#campsite
def campsite():
	x = random.randint(1,5)
	if x == 1:
		cnps1()
	if x == 2:
		cnps2()
	if x == 3:
		cnps3()
	if x == 4:
		cnps4()

def cnps1(errorCode = ""):
	if cnps1 == 1
	 	campsite()
	print("""

	You find yourself atop a hill. You stare down in awe as you realize
	how close you were to walking off the edge of the steep cliff, covered
	by sagging vines. As you slowly back from the edge and look up, you see
	an unpleasant journey ahead of you. Large gaping cracks in the ground
	and disgusting splotches in the distance, possibly those horrifying
	mutants. Reasonably, you take the time to rest and plan to be prepared.

 					  V V V
					   V V

			a) plan (+Wisdom)
			b) exersize (+Strength)
			c) search for water (Refill Bottle)
			d) set trap (-Hunger)
			e) ponder (+Cleverness)

	{}""".format(errorCode))

	response = askPrompt()

	if response == "a":
		character.addsmrt()
		clearScreen()
		("Good idea\n +1 Smarts")
		askPrompt("Press Enter to Continue...")

	elif response == "b":
		character.addStrength()
		clearScreen()
		("+1 Strenth")
		askPrompt("Press Enter to Continue...")

	elif response == "c":
		character.drink()
		clearScreen()
		("Refreshed")
		askPrompt("Press Enter to Continue...")


	elif response == "d":
		character.minhngr()
		clearScreen()
		print("""

	There we go. You take a nap. When you wake up, you aren't
	really sure if it's dawn or dusk from the clouded sky, but
	you know you caught something.

		[Cook and eat [-1 hunger]

			""")
		askPrompt("Press Enter to Continue...")

	elif response == "e":
		character.addclev()
		clearScreen()
		("Yeaaaa! I've got it\n +1 Cleverness")
		askPrompt("Press Enter to Continue...")

	else:
		cnps1("No...")
	cnps1 == 1
	roll()

def cnps2(errorCode = ""):
	if cnps2 == 1
	 	campsite()

	print("""

	As you travel through the land you look up and see a deeformed tree.
	It looks almost like it's branches were manipulated, cut, or twisted
	in some way. You look closer and see ropes and strings tightly
	clinging onto the braches. You approach the tree even closer to
	see an Emergency hammoc, ones given to your crew. It seems that it has been
	abandoned, judging from all the empty scraps of garbage. Hopeful, you start
	to wonder if you aren't the only one who has been separated. Being tired
	as you are, you climb up the tree, rest, then decide what to do.

					  V V V
					   V V

	a) Plan (+Widsom)
	b) Exersise (+Strength)
	c) Search for water (Refill Bottle)
	d) Set trap (-Hunger)
	e) Ponder (+Cleverness)

	{}
	""".format(errorCode))

	response = askPrompt()

	if response == "a":
		character.addsmrt()
		clearScreen()
		("That works\n +1 Wisdom")
		askPrompt("Press Enter to Continue...")

	elif response == "b":
		character.addStrength()
		clearScreen()
		("+1 Strenth")
		askPrompt("Press Enter to Continue...")

	elif response == "c":
		character.drink()
		clearScreen()
		("Refreshed")
		askPrompt("Press Enter to Continue...")

	elif response == "d":
		clearScreen()
		character.minhngr()
		print("""
		Trap set. You climb up the tree and go to sleep in the hammock, but
		something wakes you up. You hear something squirming in your trap.
		It looks disgusting, but it actually tasted delicious. Then again,
		everything tastes good when you are hungry.

		[Cook and eat [-1 hunger]

		""")
		askPrompt("Press Enter to Continue...")

	elif response == "e":
		character.addclev()
		clearScreen()
		print("Yeaaaa! I've got it\n +1 Cleverness")
		askPrompt("Press Enter to Continue...")


	else:
		cnps2("No...")
	cnps2 == 1
	roll()

def cnps3(errorCode = ""):
	if cnps3 == 1
	 	campsite()

	print("""

	Treading through the thick, mutated forest, you realize the forest seems
	to thin. You tread faster through the bizzar trees and bushes and behold
	a confusing sight. At first, you have a mix of feelings. Happy that the
	forest has ended. Scared of what lies ahead. But, you mostly wonder if
	it is safe. Later, you set up camp in a thick bush, carefully avoiding
	the berries, and use the burnt trees as charcoal.

					V V V
					 V V

	a) Plan (+Widsom)
	b) Exersise (+Strength)
	c) Search for water (Refill Bottle)
	d) Set trap (?)
	e) Ponder (+Cleverness)

	{}
	""".format(errorCode))

	response = askPrompt()

	if response == "a":
		character.addsmrt()
		("That works\n +1 Smarts")

	elif response == "b":
		character.addStrength()
		("+1 Strenth")

	elif response == "c":
		character.drink()
		("Refreshed!")

	elif response == "d":
		clearScreen()
		character.minhngr()
		print("""

		Trap set. You climb up the tree and go to sleep in the hammock, but
		something wakes you up. You hear something squirming in your trap.
		It looks disgusting, but it actually tasted delicious. Then again,
		everything tastes good when you are hungry.

		[Cook [+1 Food]

		""")

	elif response == "e":
		character.addclev()
		("Yeaaaa! I've got it\n +1 Cleverness")


	else:
		cnps3("No...")
	cnps3 == 1
	roll()

def cnps4(errorCode = ""):

	print("""

	Time to prepare for the night. Since you are feeling tired, you decide
	to construct your Emergency hammock and set up.

				  V V V
				   V V

			a) Plan (+Widsom)
			b) Exersise (+Strength)
			c) Search for water (Refill Bottle)
			d) Set trap (-Hunger)
			e) Ponder (+Cleverness)

	{}
	""".format(errorCode))

	response = askPrompt()

	if response == "a":
		character.addsmrt()
		clearScreen()
		("Seem about right\n +1 Smarts")
		askPrompt("Press Enter to Continue...")

	elif response == "b":
		character.addStrengthength()
		clearScreen()
		("+1 Strenth")
		askPrompt("Press Enter to Continue...")

	elif response == "c":
		character.drink()
		clearScreen()
		("Refreshed")
		askPrompt("Press Enter to Continue...")

	elif response == "d":
		clearScreen()
		character.minhngr()
		print("""
		You set a basic trap and take a nap. You wake up to find that you
		actually caught something.

			[Cook [+1 Food item]

			""")
			askPrompt("Press Enter to Continue...")

	elif response == "e":
		character.addclev()
		clearScreen()
		print("Maybe that'll work\n +1 Cleverness")
		askPrompt("Press Enter to Continue...")


	else:
		cnps4("No...")

	roll()

#creature
enc1d():
	clevbuff()
	print("""
	The Beast looks at you wearily, wondering what you plan on doing with
	drooping ears. It looks as if it is a calf separated from it's crash.

					  V V V
					   V V

			a) Leave
			b) Sneak Attack	|works - {}%|

	""".format(int(self.strength * 2), errorCode))

	response = askPrompt()
	if response = 'b'
	do_attack()

	if atk == 1
		print("""
		As you charge toward it, you feel guilty of poaching.
		You realize that it has evolved to hide from poachers
		that kill rhinos for their horns. Finally, still with
		a thoughtful doubt in your mind, you stab the beast and
		it falls to the ground with a sad final shriek. Still feeling
		inhumane, you take the rhino's horn.
		""")
	clevdebuff()

	if atk == 0
	print("""

			As you prepare to attack the rhino.
			In notices you, and with one swift
			move, it charges you and knocks you
			into a tree. You pass out immediately.

				     	  `::-----------:.
				       .::-              .::.
				    `::.                    .:-
				   ::                         `/.
				  :-                            -/
				  +./                           -:-
				 :- y                          -+ +
				 o `s                          .o o
				 o o.                           s o
				 o/: `..--`                     o.o
				 ++.odNNNNmddo` `---.  .-/y++/:``.+
				 .+:MMMMMMMMMMo ....:`+mMMMMMMMm//.
				.:-:MMMMMMMMMMN. `    NMMMMMMMMMo/.
				o` `dMMMMMMMMmo`+dd/ `NMMMMMMMMm`+`
				o   .+yhddhs:. /NMMy  -yNMMMMNy. .+
				:-             mMMMM:   .:+o+:   `+
				 /.```        oMMMMMd            /`
				  ..-+-/`     +NNmMNy      `````::
				  .::+ so      ..`:-      o-++++`
				  /.   ss`               -N `..+
				   -/` +Mms:---:-.-:-.-:sdh  /-
				     +`.MMm+oy.o.s`s++y+MM: /.
				      +`+MMMhyosoyoss+NMMo :-
				      `+ /dy+---...--:oy-  o
				       :-                `+`
				        -:--:--------:--::
		""")
		time.sleep(1000000)

def creature_enc():
	x = random.randint(1,4)
	if x == 1:
		enc1()
	if x == 2:
		enc2()
	if x == 3:
		enc3()
	if x == 4:
		enc4()

def enc1(errorCode = ""):

	if enc1 == 1
		creature_enc()
	print("""

	While treading through a thick jungle, you meet behind to face with a
	camouflage rhino. It seems to be slightly disturbed, but not aware of you.
	What will you do?

 					  V V V
					   V V

			a) RUN!!! |works - 50%|
			b) Hide |works - {}%|
			c) Encounter

		{}

	""".format(int(self.clever * 2), errorCode))

	response = askPrompt()
		if response = "c"
			print("""
			The Beast looks at you wearily, wondering what you plan on doing with
			drooping ears. It looks as if it is a calf separated from it's crash.

							  V V V
							   V V

			a) Throw him a small piece of your food and leave slowly (+ Wisdom)
			b) Pet
			c) KILL	|works - {}%|
			""".format(int(self.strength * 2), errorCode))

			response = askPrompt()
			if response = 'c'
				do_atactk()

			if atk == 1
				print("""
				As you charge toward it, you feel guilty of poaching.
				You realize that it has evolved to hide from poachers
				that kill rhinos for their horns. Finally, still with
				a thoughtful doubt in your mind, you stab the beast and
				it falls to the ground with a sad final shriek. Still feeling
				inhumane, you take the rhino's horn.
				""")
			roll()

			if atk == 0
				print("""

				As you prepare to attack the rhino.
				In notices you, and with one swift
				move, it charges you and knocks you
				into a tree. You pass out immediately.

				     	  `::-----------:.
				       .::-              .::.
				    `::.                    .:-
				   ::                         `/.
				  :-                            -/
				  +./                           -:-
				 :- y                          -+ +
				 o `s                          .o o
				 o o.                           s o
				 o/: `..--`                     o.o
				 ++.odNNNNmddo` `---.  .-/y++/:``.+
				 .+:MMMMMMMMMMo ....:`+mMMMMMMMm//.
				.:-:MMMMMMMMMMN. `    NMMMMMMMMMo/.
				o` `dMMMMMMMMmo`+dd/ `NMMMMMMMMm`+`
				o   .+yhddhs:. /NMMy  -yNMMMMNy. .+
				:-             mMMMM:   .:+o+:   `+
				 /.```        oMMMMMd            /`
				  ..-+-/`     +NNmMNy      `````::
				  .::+ so      ..`:-      o-++++`
				  /.   ss`               -N `..+
				   -/` +Mms:---:-.-:-.-:sdh  /-
				     +`.MMm+oy.o.s`s++y+MM: /.
				      +`+MMMhyosoyoss+NMMo :-
				      `+ /dy+---...--:oy-  o
				       :-                `+`
				        -:--:--------:--::
				""")
			    time.sleep(1000000)

		if response = 'b'


#safespot
def safespot():
	x = random.randint(1,4)
	if x == 1:
		ss1()
	if x == 2:
		ss2()
	if x == 3:
		ss3()
	if x == 4:
		ss4()






errorCode = ""

def findGameSave():
	my_file = Path("gameSave.sv")
	if my_file.is_file():
		return True
	else:
		return True
#Runs the welcome Screen and waits for the <Enter> key
def welcomeScreen(invalidResponse = ""):
	clearScreen()
	if findGameSave() == True:
		continuegame = "b) Continue Game"
	else:
		continuegame = ""
	print("""
		 Welcome to --==The Planet Snatcher==--
	By Dylan Starink and Frank Dinnino

	  a) New Game
	  {}

		 {}
	""".format(continuegame,invalidResponse))
	letter = askPrompt()
	if letter == "a":
		#Overwrite Game Save and Start new Game
		pass
	elif letter == "b":
		if findGameSave == False:
			welcomeScreen("Invalid Response")

		#Start Last game
		pass
	else:
		welcomeScreen("Invalid Response")
def clearScreen():
	if opsys == 1:
		os.system("cls")
	elif opsys >= 2 & opsys <= 3 | opsys > 4 :
		os.system("clear")
	elif opsys == 4:
		import console
		console.clear

#Loading(Time to Load, Optional: Amount of Loading, Optional: Time per Loading Section)
def Wait(text,sec, amount = 3, tpl = 4):
	count = 0
	tpl = tpl * amount
	while count < amount:
		clearScreen()
		print(text)
		time.sleep(sec/tpl)
		clearScreen()
		print("Loading.")
		time.sleep(sec/tpl)
		clearScreen()
		print("Loading..")
		time.sleep(sec/tpl)
		clearScreen()
		print("Loading...")
		time.sleep(sec/tpl)
		count += 1

#Asks for Input and Returns it
def askPrompt(Uinput = ">> "):
	ask = input(Uinput)
	return ask

#Runs the setup character screen
def enterCharacter(errorCode=""):
	clearScreen()
	print("""
	----===Enter Character===----

	a) Native
	b) Soldier
	c) Pilot
	d) Debug


		 {}
	""".format(errorCode))
	character = askPrompt()
	if character == "a":
		print("\nMage Selected")
	elif character == "b":
		print("\nKnight Selected")
	elif character == "c":
		print("\nWizard Selected")
	elif character == "d":
		print("\nDebug Selected")
	else:
		enterCharacter("Invalid Reponse")

#  1- Windows, 2 - Mac, 3 - Linux, 4 - IOS, 99 - Unknown
if sys.platform == "win32":
	opsys = 1
elif sys.platform == "darwin":
	opsys = 2
elif sys.platform == "linux2":
	opsys = 3
elif sys.platform == "ios":
	opsys = 4
else:
	opsys = 99

welcomeScreen()
enterCharacter()
campsite()
