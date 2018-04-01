class campsite():

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
