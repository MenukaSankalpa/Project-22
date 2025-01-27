#-Loop
#--ask: roll the game ?
#--if user enter y
#----generate two numbers 
#----print them
#--If user enter n
#----print thank you msg
#----terminate game
#--else
#----print invalid choice 
import random

while True:
 choice = input('Roll the Dice? (y/n): ').lower()
 if choice == 'y':
     die1 = random.randint(1, 6)
     die2 = random.randint(1, 6)
     print(f'({die1}, {die2})')
 elif choice == 'n':
     print('Thank for playing!')
     break
 else: 
     print('Invalid choice')