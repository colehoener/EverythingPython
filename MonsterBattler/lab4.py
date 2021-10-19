#Mark Boady and Matthew Burlick
#Drexel University 2018
#CS 172

from kraken import kraken
from urmom import urmom
from Medlock import medlock
from depression import depression
import random

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

	#first reset everyone's health!
	m1.resetHealth()
	m2.resetHealth()

	#next print out who is battling
	print("Starting Battle Between")
	print(m1.getName()+": "+m1.getDescription())
	print(m2.getName()+": "+m2.getDescription())
	print()
	
	
	#Whose turn is it?
	attacker = None
	defender = None
	
	#Select Randomly whether m1 or m2 is the initial attacker
	#to other is the initial definder
	num = random.randint(1,3)
	if(num == 1):
		attacker = m1
		defender = m2
	else:
		attacker = m2
		defender = m1
	
	print(attacker.getName()+" goes first.")
	#Loop until either 1 is unconscious or timeout
	while( m1.getHealth() > 0 and m2.getHealth() > 0):
		#Determine what move the monster makes
		#Probabilities:
		#	60% chance of standard attack
		#	20% chance of defense move
		#	20% chance of special attack move

		#Pick a number between 1 and 100
		move = random.randint(1,100)
		#It will be nice for output to record the damage done
		before_health=defender.getHealth()
		
		#for each of these options, apply the appropriate attack and 
		#print out who did what attack on whom
		if( move >=1 and move <= 60):
			attacker.basicAttack(defender)
			print(attacker.getName() + " used " + attacker.basicName() + " on " + defender.getName())
		elif move>=61 and move <= 80:
			#Defend!
			attacker.defenseAttack(defender)
			print(attacker.getName() + " used " + attacker.defenseName() + " on " + defender.getName())
		else:
			#Special Attack!
			attacker.specialAttack(defender)
			print(attacker.getName() + " used " + attacker.specialName() + " on " + defender.getName())
		
		#Swap attacker and defender
		m3 = attacker
		attacker = defender
		defender = m3
		
		#Print the names and healths after this round
		print(m1.getName() + " at " + str(m1.getHealth()))
		print(m2.getName() + " at " + str(m2.getHealth()))
		print()

		
	#Return who won
	if m1.getHealth() <= 0:
		return m2
	elif m2.getHealth() <= 0:
		return m1

#----------------------------------------------------
if __name__=="__main__":
	#Every battle should be different, so we need to
	#start the random number generator somewhere "random".
	#With no input Python will set the seed
	
	random.seed(0)

	#First round
	print("Round 1\n")
	first = kraken("Squid Boi")
	second = urmom("Mother")
	
	winner1 = monster_battle(first,second)
	
	#Print out who won
	print(winner1.getName() + " is victorious!")

	#Round 2
	print("\n----------\nRound 2\n")
	first = medlock("Professor Medlock")
	second = depression("Depression")

	winner2 = monster_battle(first,second)
	
	#Print out who won
	print(winner2.getName() + " is victorious!")

	#Championship
	print("\n----------\nChampionship\n")
	first = winner1
	second = winner2

	winner = monster_battle(first,second)
	
	#Print out who won
	print(winner.getName() + " is victorious!")
	