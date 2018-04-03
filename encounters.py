import random
class encounters:
	def __init__(self):
		self.getJson()


	def getJson(self,jsonFile = "settings.json"):
		with open(jsonFile,"r") as file:
			Dictionary = json.load(file)
			self.StoryData = Dictionary


	def creature_enc(self):
		x = random.randint(1,4)
		if x == 1:
			enc1()
		if x == 2:
			enc2()
		if x == 3:
			enc3()
		if x == 4:
			enc4()



	def printOptions(self,list = ["RUN!!! |works - 50%|","Hide \*s","Encounter","Attack \*r","shout"]):

		alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]
		count = 0
		for x in list:
				if "(s)" in x:
					print(alphabet[count]+") " + x.strip("(s)") + " |Works - {}%|".format(character.strength*2))
				if "(c)" in x:
					print(alphabet[count]+") " + x.strip("(c)") + " |Works - {}%|".format(character.clever*2) )
				else:
					print(alphabet[count]+") " + x)
				count += 1
	def printRandomStory(self):
		storyID = (random.randint(1,len(self.StoryData["RandomStories"])))-1
		print(self.StoryData["RandomStories"][storyID]["TEXT"])
		return StoryID

	def doAction(self,storyID,actionNumber,Random = True):
		optionState = "SUCCESS"
		if Random = True:
			execData = self.StoryData["RandomStories"][storyID]["OPTIONS"]
		else:
			execData = self.StoryData["Stories"][storyID]["OPTIONS"]
		if "PERCENT" in execData:
			percent = execData["PERCENT"]
			if random.randint(1,100) <= percent:
				pass
				]
			else:
				optionState = "FAILED"
		try:
			for x in execData[optionState]:
				for i in ["SHOW","BUFF"]
					try:
						Command = x[i]
						exec("self." + i.lower() + "("Command")")
					except:
						pass
		except:
			pass






	def printStorys(self,number):
		story = ["""
		While treading through a thick jungle, you meet behind to face with a
		camouflage rhino. It seems to be slightly disturbed, but not aware of you.
		What will you do?
		""",
		"""
		The Beast looks at you wearily, wondering what you plan on doing with
		drooping ears. It looks as if it is a calf separated from it's crash.
		""",
		"""
		As you charge toward it, you feel guilty of poaching.
		You realize that it has evolved to hide from poachers
		that kill rhinos for their horns. Finally, still with
		a thoughtful doubt in your mind, you stab the beast and
		it falls to the ground with a sad final shriek. Still
		feeling inhumane, you take the rhino's horn.
		""",

		]




		insert = """

			 		  	   V V V
					   		V V

				"""








	def enc1(self,errorCode = ""):

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
				c) Attack	\*
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
					it falls to the ground with a sad final shriek. Still
					feeling inhumane, you take the rhino's horn.
					""")
				roll()

				if atk == 0
					print("""

					As you prepare to attack the rhino.
					In notices you, and with one swift
					move, it charges you and knocks you
					into a tree. You pass out immediately.

						 	  `::-----------:.
						   .::-			     .::.
						`::.					.:-
					   ::					   	  `/.
					  :-							-/
					  +./						   -:-
					 :- y						  -+ +
					 o `s						  .o o
					 o o.						   s o
					 o/: `..--`					 o.o
					 ++.odNNNNmddo` `---.  .-/y++/:``.+
					 .+:MMMMMMMMMMo ....:`+mMMMMMMMm//.
					.:-:MMMMMMMMMMN. `	  NMMMMMMMMMo/.
					o` `dMMMMMMMMmo`+dd/ `NMMMMMMMMm`+`
					o   .+yhddhs:. /NMMy  -yNMMMMNy. .+
					:-			   mMMMM:   .:+o+:   `+
					 /.```		  oMMMMMd			  /`
					  ..-+-/`	  +NNmMNy	  `````::
					  .::+ so	  ..`:-	      o-++++`
					  /.   ss`			    -N `..+
					   -/` +Mms:---:-.-:-.-:sdh  /-
						 +`.MMm+oy.o.s`s++y+MM: /.
						  +`+MMMhyosoyoss+NMMo :-
						  `+ /dy+---...--:oy-  o
						   :-				`+`
							-:--:--------:--::
					""")
					time.sleep(1000000)

			if response = 'b'
				Print_1





	#creature encounter

Screen = encounters()
