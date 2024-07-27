import sys
from rps7 import rps
from guess_num import gn

def arcade(name= 'PlayerOne'):
    play_arcade = False

    while True:
        if play_arcade == True:
            print(f"\n{name}, welcome to the arcade menu")

        playerchoice = input(
            f"\n{name}, Please choose a game:\n 1 =Rock Paper Scissors\n 2 = Guess My number\n\n Or press \"x\" to exit the Arcade\n\n"
        )

        if playerchoice not in ["1", "2", "x"]:
            print(f"{name}, please enter 1, 2, or x.")
            return arcade(name)
        
        play_arcade = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = gn(name)
            guess_my_number()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🎮")

    arcade(args.name)

  

 


        



    