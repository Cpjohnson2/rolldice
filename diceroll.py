from random import randint
masterdice=[4,6,8,10,12,20]
dice1=[4,6,8,10,12,20]
dice2=[4,6,8,10,12,20]
#this is the number of dice (6) and how many sides are on each dice

# this section defines some variables
choice1= 0
choice2= 0 
score1 = 0 
score2 = 0
roundover = False

#this section we get players to select a die and we verify that their choice is valid
print dice1
while choice1 not in dice1:
	choice1=raw_input("Player1 choose your die:")
	if choice1.isalnum() and choice1.isalpha()==False: #<------ fix this for alnum
		choice1=int(choice1)
print dice2
while choice2 not in dice2:
	choice2= int(raw_input("Player2 choose your die:"))
	
#this section we roll the dice that were selected	
roll1= randint(1,choice1)
print "player1 rolls a", roll1
roll2= randint(1,choice2)
print "player2 rolls a", roll2

#here we test if either player rolled a 1 or 2
if roll1 == 1: 
	roundover = True 
	
if roll2 == 1: 
	roundover = True 

if roll1 == 2: 
	score1 = score1-1
	roundover = True 
	
if roll2 == 2: 
	score2 = score2-1
	roundover = True 

#if neither player rolled a 1 or 2 we test to see who won (if anyone)	
if roundover==False: 
	if roll1 > roll2: 
		score1=score1+1
	elif roll1 < roll2: 
		score2=score2+1
	else: 
		print "it's a tie"

#prints out the Round Summary
print "\n=============\nRound Summary\n=============\n"
print "Player1 started with these dice:",dice1,"\n","and chose to roll the D",choice1,"\n\n"
print "Player2 started with these dice:",dice2,"\n","and chose to roll the D",choice2,"\n\n"
print "Player1 rolled a",roll1,"and Player2 rolled a",roll2
print "The current score:"
print "Player1 =",score1
print "Player2 =",score2

#check for a winner
if roll1==1 or roll2==1:
	print "Whoa! Someone rolled a 1!"
	if roll1==roll2:
		print "...but it was both players, so it's on to the next round."
		gameOver=False
	elif roll1==1:
		print "...and it was Player1! Player1 wins!"
		gameOver==True

		

	
#regardless of roll outcome, we remove the last rolled dice from playable dice
dice1.remove(choice1)
dice2.remove(choice2)	
		
