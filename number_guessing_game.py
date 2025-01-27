#generate a random number
#Loop
 #-ask the user to make guess
 #-if not valid number
 #--print an error
 #-if number < guess
 #--print too low
 #-if number > guess
 #--print to high
 #-else 
 #--print well done

import random

number_to_guess = random.randint(1, 100)
while True:
 try:
     guess = int(input('Guess the number between 1 and 100: '))
     
     if guess < number_to_guess:
         print('To low!')
     elif guess > number_to_guess:
         print('To high!')
     else:
         print('Congratulations! You won the game.')
         break    
     
 except ValueError:
     print('Please enter valid number')       

