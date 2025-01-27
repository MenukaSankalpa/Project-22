#ask the user to make a choice
#if choice is not valid
# print an error
#let computer to make choice
#print choices
#determined the winner
#ask the user if they want to continue
#if not
#terminate
import random

choices = ['r', 'p', 's']
user_choice = input('Rock, Paper or Scissors? (r,p,s): ').lower()

if user_choice not in choices:
    print('Invalid choice!')
computer_choice = random.choice(choices)
print(f'You chose {user_choice}')
print(f'Computer chose {computer_choice}')