from random import randint
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


player_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))

computer_choice = randint(0, 2)

choices = [rock, paper, scissors]

if player_choice >= 3 or player_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(choices[player_choice])
    print(f"Computer chose: \n {choices[computer_choice]}")

    if player_choice == computer_choice:
        print("Draw")
    elif player_choice == 0:
        if computer_choice == 2:
            print("You win!")
        else:
            print("You lose.")
    elif player_choice == 1:
        if computer_choice == 0:
            print("You win!")
        else:
            print("You lose.")
    elif player_choice == 2:
        if computer_choice == 1:
            print("You win!")
        else:
            print("You lose.")
