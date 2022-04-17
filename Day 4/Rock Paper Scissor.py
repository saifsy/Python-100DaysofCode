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

#Write your code below this line 👇
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
print(type(user_choice))
randomlist=[rock,paper,scissors]
randomchoice=random.choice(randomlist)
if (user_choice=="0" and randomchoice == scissors):
  user_choice = rock
  print(f"{user_choice} \n {scissors} \n You WIN")
elif (user_choice=="0" and randomchoice == paper):
  user_choice = rock
  print(f"{user_choice} \n {paper} \n You LOSE")
elif(user_choice=="0" and randomchoice == rock):
  user_choice = rock
  print(f"{user_choice} \n {rock} \n DRAW")