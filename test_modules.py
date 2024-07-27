
# from rps7 import run
# from guess_number import play
# from enum import Enum


# def arcade(name='PlayerOne'):
#      def play_arcade():
#         nonlocal name

#         class ARCADE(Enum):
#                     play()   = 1
#                     run()   = 2 

#         playerchoice = input(f"\n{name}, Please choose a game:\n 1 =Rock Paper Scissors \n 2 = Guess My number \n Or press 'x' to exit the Arcade\n")
        

#         if playerchoice not in ["1", "2", "3"]:
#             print(f"{name}, please enter 1, 2, or 3.")
#             return Play_arcade()
                

# if __name__ == "__main__":
#     import argparse

#     parser = argparse.ArgumentParser(
#         description="Provides a personalized game experience."
#     )

#     parser.add_argument(
#         "-n", "--name", metavar="name",
#         required=True, help="The name of the person playing the game."
#     )

#     args = parser.parse_args()

#     play = rps(args.name)
#     play()               

 # py arcade.py -n "Val"