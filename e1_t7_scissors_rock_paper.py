'''
Task 7: Scissors, Rock, Paper

Exercise 3.17 in Liang is about the famous game scissors, rock, paper. Implement the game according to the instructions in the book, where a scissor can cut paper, a rock knocks a scissor and a paper can wrap a rock. Use the integers 0, 1 and 2 to represent scissors, rock and paper respectively. As usual, see an example execution below:

Enter your choice (0 for scissors, 1 for rock, 2 for paper):  2
Your choice: paper
Computer's choice: scissors
You lose!
'''

# Code Starts:

import random

user_choice = int(input('Enter your choice (0 for scissors, 1 for rock, 2 for paper): '))
computer_choice = random.randint(0, 2)

scissors = 0
rock = 1
paper = 2


if user_choice == 0 and computer_choice == 0:
    print('Your choice: scissors')
    print("Computer's choice: scissors")
    print('It is a draw!')
elif user_choice == 0 and computer_choice == 1:
    print('Your choice: scissors')
    print("Computer's choice: rock")
    print('You lose!')
elif user_choice == 0 and computer_choice == 2:
    print('Your choice: scissors')
    print("Computer's choice: paper")
    print('You win!')
elif user_choice == 1 and computer_choice == 0:
    print('Your choice: rock')
    print("Computer's choice: scissors")
    print('You win!')
elif user_choice == 1 and computer_choice == 1:
    print('Your choice: rock')
    print("Computer's choice: rock")
    print('It is a draw!')
elif user_choice == 1 and computer_choice == 2:
    print('Your choice: rock')
    print("Computer's choice: paper")
    print('You lose!')
elif user_choice == 2 and computer_choice == 0:
    print('Your choice: paper')
    print("Computer's choice: scissors")
    print('You lose!')
elif user_choice == 2 and computer_choice == 1:
    print('Your choice: paper')
    print("Computer's choice: rock")
    print('You win!')
elif user_choice == 2 and computer_choice == 2:
    print('Your choice: paper')
    print("Computer's choice: paper")
    print('It is a draw!')
else:
    print('Invalid input! Please enter 0, 1, or 2.')

# Second vision:

import random

choice = int(input('Enter your choice (0 for scissors, 1 for rock, 2 for paper):  '))

if choice == 0:
    print('Your choice: scissors')
elif choice == 1:
    print('Your choice: rock')
else:
    print('Your choice: paper')

pc_choice = random.randint(0, 2)

if pc_choice == 0:
    print("Computer's choice: scissors")
elif pc_choice == 1:
    print("Computer's choice: rock")
else:
    print("Computer's choice: paper")

if choice == pc_choice:
    print('Tie!')
elif (choice == 0 and pc_choice == 2) or \
     (choice == 1 and pc_choice == 0) or \
     (choice == 2 and pc_choice == 1):
    print('You Win!')
else:
    print('You lose!')