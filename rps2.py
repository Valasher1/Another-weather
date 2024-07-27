import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3   

playagain = True

while playagain:
    
    playerchoice = input("\n Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

    player = int(playerchoice)

    if player  < 1 or player  > 3:
        sys.exit("You must enter 1, 2, or 3.")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

   
    print("\nYou choose" + str(RPS(player)).replace('RPS.', " ") + ".")
    print("Python choose" + str(RPS(computer)).replace('RPS.', " ") + ".\n")
   

    if player == 1 and computer == 3:
        print("🎉 You win!\n")
       
    elif player == 2 and computer == 1:
        print("🎉 You win!\n")
       
    elif player == 3 and computer == 2:
        print("🎉 You win!\n")
        
    elif player == computer:
        print("😲 Tie game!\n")
       
    else:
        print("🐍 Python wins!\n")
       

    playagain =  input("\n Play again? \nY for yes \nQ for quit \n\n") 

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye! 🙋‍♂️🙋‍♀️\n")

