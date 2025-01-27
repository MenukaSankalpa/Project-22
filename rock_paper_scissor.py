#ask the user to make a choice
#if choice is not valid
# print an error
#let computer to make choice
#print choices
#determined the winner
#ask the user if they want to continue
#if not
#terminate
#key value
import random

while True: 
 emojis = {'r': '🪨', 'p': '📃', 's': '✂️' }
 choices = ['r', 'p', 's']
 
 user_choice = input('Rock, Paper or Scissors? (r, p, s): ').lower()
 if user_choice not in choices: 
    print('Invalid choice!')
    continue
     
 computer_choice = random.choice(choices)
 
 print(f'You chose => {emojis[user_choice]}')
 print(f'Computer chose => {emojis[computer_choice]}')
 
 if user_choice == computer_choice:
     print('Tie!')
 elif (
     (user_choice == 'r' and computer_choice == 's') or 
     (user_choice == 's' and computer_choice == 'p') or 
     (user_choice == 'p' and computer_choice == 'r')):
    print('You win')
 else:
     print('You lose')    

 should_continue = input('Continue? (y/n): ').lower()
 if should_continue == 'n':
     break