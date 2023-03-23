import random

rps = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
# END OF SECTION 👆

# WRITE YOUR CODE BELOW THIS LINE 👇
while True:
  # list of choices 
  computer_choices = ['rock','paper','scissors']

  # Ask for input
  user_choice = input("what your choice ('rock','paper','scissors') ").strip().lower()


  if user_choice == 'quit':
    break
# computer make a choice
  computer_choice = random.choice(computer_choices)

  print()
# print out ascii art for the user
  print('You chose: ')
  if user_choice == 'rock':
    print(rps[0])
  if user_choice == 'paper':
    print(rps[1])
  if user_choice == 'scissors':
    print(rps[2])

# print out ascii art for the computer
  print('Computer chose: ')
  if computer_choice == 'rock':
    print(rps[0])
  if computer_choice == 'paper':
    print(rps[1])
  if computer_choice == 'scissors':
    print(rps[2])

# Deciding who wins
    # when computer choose rock
  if computer_choice == 'rock' and user_choice == 'rock':
    print('Its a tie')
  if computer_choice == 'rock' and user_choice == 'paper':
    print('You win 🏆. Paper covers Rock')
  if computer_choice == 'rock' and user_choice == 'scissors':
    print('You lose 😢. Rock smashes scissors')

# Computer chooses paper
  if computer_choice == 'paper' and user_choice == 'paper':
   print('its a tie')
  if computer_choice == 'paper' and user_choice =='rock':
   print('Computer wins Paper covers rock')
  if computer_choice == 'paper' and user_choice == 'scissors':
   print('You win Scissors cut paper')
  # computer chooses scissors
  if computer_choice=='scissors' and user_choice =='scissors' :
   print('its a tie')
  if computer_choice =='scissors' and user_choice =='paper' :
   print('computer wins scissors cut paper')
  if computer_choice =='scissors' and user_choice =='rock' :
   print('you win rock smashes scissors')

