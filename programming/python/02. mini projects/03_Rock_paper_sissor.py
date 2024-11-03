
# Rock Paper Scissors Game :

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

"""
0 - Rock
1 - Paper
2 - Scissors

"""

"""
User_Choice = int(input("What Do You Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))

# print("User Choice : ",User_Choice)


Computer_Choice = random.randint(0 , 2)

# print("Computer Choice : ",Computer_Choice)


game = [rock,paper,scissors]

if User_Choice>=3 or User_Choice <0: # 3456 or -1-2
    print("You Type Wrong")

else:

    print("User Choose : \n",game[User_Choice] )

    print("Computer Choose : \n",game[Computer_Choice])

    if User_Choice == 0 and  Computer_Choice == 2: #  Rock - Scissors
        print("Rock Smashes Scissors! You Win!")

    elif Computer_Choice == 0 and User_Choice == 2: #  C => Rock - U => Scissors
        print("Rock Smashes Scissors! You Lose!")

    elif Computer_Choice > User_Choice : # C => 1 2 -  U => 0 1
        print("You Lose!")

    elif User_Choice > Computer_Choice : # U => 1 2  -  C => 0 1
        print("You Win!")

    elif User_Choice == Computer_Choice :
        print("It's a Tie!")


"""