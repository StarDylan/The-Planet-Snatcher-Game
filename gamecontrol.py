import random
import os

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"]

class encounters:
    def __init__(self):
        pass

    #Import JsonFile
    # Dictionary = getJson(fileToReadFrom)
    def getJson(self,jsonFile):
        with open(jsonFile,"r") as file:
            return json.load(file)
    def randomCatagory(self):
        listFolders = os.listdir("RandomStories")
        randomIndex = randint(0,len(listFolders)-1)
        return listFolders[randomIndex]

    #Start a story line from files.
    def startRandomStory(self,category):
        #Find all Files in folder
     	fileList = os.listdir("RandomStories\{}".format(category))
        chosenStory = randint(0,len(fileList)-1)

        storyDict = getJson("RandomStories\{}\{}".format(category, fileList[chosenStory]))

        print(storyDict["TEXT"])
        for optionIndex in storyDict["OPTIONS"]:
            option = storyDict["OPTIONS"][optionIndex].keys()[0]
            print("{}) {}".format(alphabet[optionIndex],option))






#pass in randomCatagory() as catagory
startRandomStory(randomCatagory())



    #
    # def printOptions(self,list = ["RUN!!! |works - 50%|","Hide \*s","Encounter","Attack \*r","shout"]):
    #
     #
    # 	count = 0
    # 	for x in list:
    # 			if "(s)" in x:
    # 				print(alphabet[count]+") " + x.strip("(s)") + " |Works - {}%|".format(character.strength*2))
    # 			if "(c)" in x:
    # 				print(alphabet[count]+") " + x.strip("(c)") + " |Works - {}%|".format(character.clever*2) )
    # 			else:
    # 				print(alphabet[count]+") " + x)
    # 			count += 1
    # def printRandomStory(self,group = "Encounters"):
    # 	storyUID = (random.randint(1,len(self.StoryData["RandomStories"][group])))-1
    # 	print(self.StoryData["RandomStories"][group][storyUID]["TEXT"])
    # 	return storyUID
    #
    # def doAction(self,storyUID,actionNumber,group,Random = True):
    # 	optionState = "SUCCESS"
    # 	if Random == True:
    # 		execData = self.StoryData["RandomStories"][group][storyUID]["OPTIONS"]
    # 	else:
    # 		execData = self.StoryData["Stories"][storyUID]["OPTIONS"]
    # 	if "PERCENT" in execData:
    # 		percent = execData["PERCENT"]
    # 		if random.randint(1,100) <= percent:
    # 			pass
    #
    # 		else:
    # 			optionState = "FAILED"
    # 	try:
    # 		for x in execData[optionState]:
    # 			for i in ["SHOW","BUFF"]:
    # 				try:
    # 					Command = x[i]
    # 					exec("self." + i.lower() + "(" + Command + ")")
    # 				except:
    # 					pass
    # 	except:
    # 		pass



#
#
#
# 	def printStorys(self,number):
# 		story = ["""
# 		While treading through a thick jungle, you meet behind to face with a
# 		camouflage rhino. It seems to be slightly disturbed, but not aware of you.
# 		What will you do?
# 		""",
# 		"""
# 		The Beast looks at you wearily, wondering what you plan on doing with
# 		drooping ears. It looks as if it is a calf separated from it's crash.
# 		""",
# 		"""
# 		As you charge toward it, you feel guilty of poaching.
# 		You realize that it has evolved to hide from poachers
# 		that kill rhinos for their horns. Finally, still with
# 		a thoughtful doubt in your mind, you stab the beast and
# 		it falls to the ground with a sad final shriek. Still
# 		feeling inhumane, you take the rhino's horn.
# 		""",
#
# 		]
#
#
#
#
# 		insert = """
#
# 			 		  	   V V V
# 					   		V V
#
# 				"""
#
#
#
#
#
#
#
#
# 	def enc1(self,errorCode = ""):
#
# 		if enc1 == 1
# 			creature_enc()
# 		print("""
#
# 		While treading through a thick jungle, you meet behind to face with a
# 		camouflage rhino. It seems to be slightly disturbed, but not aware of you.
# 		What will you do?
#
# 	 					  V V V
# 						   V V
#
#
# 				a) RUN!!! |works - 50%|
# 				b) Hide |works - {}%|
# 				c) Encounter
#
# 			{}
#
# 		""".format(int(self.clever * 2), errorCode))
#
# 		response = askPrompt()
# 			if response = "c"
# 				print("""
# 				The Beast looks at you wearily, wondering what you plan on doing with
# 				drooping ears. It looks as if it is a calf separated from it's crash.
#
# 								  V V V
# 								   V V
#
# 				a) Throw him a small piece of your food and leave slowly (+ Wisdom)
# 				b) Pet
# 				c) Attack	\*
# 				""".format(int(self.strength * 2), errorCode))
#
# 				response = askPrompt()
# 				if response = 'c'
# 					do_atactk()
#
# 				if atk == 1
# 					print("""
# 					As you charge toward it, you feel guilty of poaching.
# 					You realize that it has evolved to hide from poachers
# 					that kill rhinos for their horns. Finally, still with
# 					a thoughtful doubt in your mind, you stab the beast and
# 					it falls to the ground with a sad final shriek. Still
# 					feeling inhumane, you take the rhino's horn.
# 					""")
# 				roll()
#
# 				if atk == 0
# 					print("""
#
# 					As you prepare to attack the rhino.
# 					In notices you, and with one swift
# 					move, it charges you and knocks you
# 					into a tree. You pass out immediately.
#
# 						 	  `::-----------:.
# 						   .::-			     .::.
# 						`::.					.:-
# 					   ::					   	  `/.
# 					  :-							-/
# 					  +./						   -:-
# 					 :- y						  -+ +
# 					 o `s						  .o o
# 					 o o.						   s o
# 					 o/: `..--`					 o.o
# 					 ++.odNNNNmddo` `---.  .-/y++/:``.+
# 					 .+:MMMMMMMMMMo ....:`+mMMMMMMMm//.
# 					.:-:MMMMMMMMMMN. `	  NMMMMMMMMMo/.
# 					o` `dMMMMMMMMmo`+dd/ `NMMMMMMMMm`+`
# 					o   .+yhddhs:. /NMMy  -yNMMMMNy. .+
# 					:-			   mMMMM:   .:+o+:   `+
# 					 /.```		  oMMMMMd			  /`
# 					  ..-+-/`	  +NNmMNy	  `````::
# 					  .::+ so	  ..`:-	      o-++++`
# 					  /.   ss`			    -N `..+
# 					   -/` +Mms:---:-.-:-.-:sdh  /-
# 						 +`.MMm+oy.o.s`s++y+MM: /.
# 						  +`+MMMhyosoyoss+NMMo :-
# 						  `+ /dy+---...--:oy-  o
# 						   :-				`+`
# 							-:--:--------:--::
# 					""")
# 					time.sleep(1000000)
#
# 			if response = 'b'
# 				Print_1
#
#
#
#
#
# 	#creature encounter
#
# Screen = encounters()
