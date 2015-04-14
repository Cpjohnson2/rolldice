from random import randint
masterdice=[4,6,8,10,12,20]
dice1=[4,6,8,10,12,20]
dice2=[4,6,8,10,12,20]
#this is the number of dice (6) and how many sides are on each dice

print dice1
choice1= 0
choice2= 0 
score1 = 0 
score2 = 0
roundover = 0
while choice1 not in dice1:
	choice1= int(raw_input("Player1 choose your die"))
print dice2
while choice2 not in dice2:
	choice2= int(raw_input("Player2 choose your die"))
roll1= randint(1,choice1)
print "player1 rolls a", roll1
roll2= randint(1,choice2)
print "player2 rolls a", roll2
if roll1 == 1: 
	score1 = score1+1
	roundover = 1 
	
if roll2 == 1: 
	score2 = score2+1
	roundover = 1 

if roll1 == 2: 
	score1 = score1-1
	roundover = 1 
	
if roll2 == 2: 
	score2 = score2-1
	roundover = 1 
	
if roundover != 1: 
	if roll1 > roll2: 
		score1=score1+1
	else: 
		if roll1 < roll2: 
			score2=score2+1
		else: 
			print "it's a tie"
			
		
		
