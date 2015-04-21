# import require libraries
from random import randint
import os
import sys
# define variables
players=[0,1]
names=["P1","P2"]
masterdice=[4,6,8,10,12,20]
dice=[[],[]] #
choice=[0,0]
gameScore=[0,0]
matchScore=[0,0]
roll=[0,0]

#A function to end everything
def quitGame():
	print "Fine, quitter. I didn't wanna play anymore with you anyway."
	raw_input("Hit 'Enter' to make this all go away...")
	os.system('cls')
	sys.exit()
def round(matchScore):
	gameOver=False
	someoneRolledSpecial = False
	while gameOver==False:
		#repopulate empty dice lists
		if len(dice[0])==0:
			for n in players:
				dice[n]=masterdice[:]
			
		#this section we get players to select a die and we verify that their choice is valid
		for n in players:
			while choice[n] not in dice[n]:
				print ".==.==.==.==.==.==.\n{0}\n'=='=='=='=='=='=='".format(formatDice(dice[n]))
				choice[n]=raw_input("{0} choose your die:".format(names[n]))
				if choice[n]=="q":
					shouldQuit=quitGame()
				try:
				 choice[n]=int(choice[n])
				except:
					print "that's not a die"
		#this section we roll the dice that were selected
		for n in players:
			roll[n]= randint(1,choice[n])
			print "{0} rolls a {1}.".format(names[n],roll[n])
		#here we test if either player rolled a 1 or 2
		for n in players:
			if roll[n] == 1: 
				someoneRolledSpecial = True 
			if roll[n] == 2 and roll[abs(n-1)]<>2: 
				gameScore[n] = gameScore[n]-1
				someoneRolledSpecial = True 
		#if neither player rolled a 1 or 2 we test to see who won (if anyone)	
		if someoneRolledSpecial==False: 
			if roll[0] > roll[1]: 
				gameScore[0]=gameScore[0]+1
			elif roll[0] < roll[1]: 
				gameScore[1]=gameScore[1]+1
			else: 
				print "it's a tie"
		displaySummary(dice,choice,roll,gameScore,matchScore,names,players)
		#check if someone won by rolling a 1
		if roll[0]==1 or roll[1]==1:
			print "Whoa! Someone rolled a 1!"
			if roll[0]==roll[1]:
				print "...but it was both players, so it's on to the next round."
				gameOver=False
			elif roll[0]==1:
				print "...and it was Player1! Player1 wins!"
				gameOver=True
			else:
				print "...and it was Player2! Player2 wins!"
				gameOver=True
		#check if someone won by getting a gameScore of -1		
		if gameOver==False:
			for n in players:
				if gameScore[n]==-1:
					print "{0}, you are so bad that you're good! You win the match with a negative gameScore!".format(names[n])
					gameOver=True
		#check if someone won by getting a gameScore of 2		
		if gameOver==False:
			for n in players:
				if gameScore[n]==2:
					print "{0}, your persistence has been rewarded. You win the match with the highest gameScore!".format(names[0])
					gameOver=True
		#regardless of roll outcome, we remove the last rolled dice from playable dice
		for n in players:
			dice[n].remove(choice[n])
			
	
def formatDice(Dice):
	diceString=[]
	for x in masterdice:
		if x in Dice:
			diceString.append(str(x))
		else:
			diceString.append("  ")
	return "|{0:>2}|{1:>2}|{2:>2}|{3:>2}|{4:>2}|{5:>2}|".format(diceString[0],diceString[1],diceString[2],diceString[3],diceString[4],diceString[5])

def displaySummary(dice,choice,roll,gameScore,matchScore,names,players):
	#prints out the Round Summary
	os.system('cls')
	print '{:^78}'.format("Round Results"),
	print '{:^80}'.format("============="),
	print '{0:^39}{1:^40}'.format(names[0],names[1]),
	print '{0:^39}{1:^40}'.format(".==.==.==.==.==.==.",".==.==.==.==.==.==."),
	print '{0:>29}{1:^20}{2:<30}'.format(formatDice(dice[0]),"Starting Dice",formatDice(dice[1])),
	print '{0:^39}{1:^40}'.format("'=='=='=='=='=='=='","'=='=='=='=='=='=='")
	print '{0:>11}{1}{2}{3}{4:^22}{5}{6}{7}'.format(" ","   "*masterdice.index(choice[0]),"[]","   "*(5-masterdice.index(choice[0])),"Chosen Die","   "*masterdice.index(choice[1]),"[]","   "*(5-masterdice.index(choice[1])))
	print
	print '{0:>20}{1:^39}{2}'.format(roll[0],"Roll Result  ",roll[1])


round(matchScore)

