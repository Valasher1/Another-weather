# import random
# import sys
# from enum import Enum

# def gn(name='PlayerOne'):
#     game_count    = 0
#     player_wins   = 0

#     def play_gn():
#         nonlocal name
#         nonlocal player_wins

#         class GN(Enum):
#             One   = 1
#             Two   = 2 
#             Three = 3 

#         playerchoice = input(f"\n{name}, guess which number I'm thinking of ... 1, 2, or 3: \n")

#         if playerchoice not in ["1", "2", "3"]:
#             print(f"{name} you must enter 1, 2, or 3.")
#             return play_gn()

#         player = int(playerchoice)

#         computerchoice = random.choice("123")
#         computer = int(computerchoice)

#         print(f"\n{name}, you choose {str(GN(player)).replace('GN.', " ")}.")
        
#         print(f"I was thinking about the number  {str(GN(computer)).replace('GN.', " ")}.\n")

#         def decide_winner(player, computer):
#             nonlocal name
#             nonlocal player_wins

#             if player == 1 and computer == 1:
#                 player_wins += 1
#                 return f"🎉 {name}, you win!\n"

#             elif player == 2 and computer == 2:
#                 player_wins += 1
#                 return f"🎉 {name}, you win!\n"

#             elif player == 3 and computer == 3:
#                 player_wins += 1
#                 return f"🎉 {name}, you win!\n"

#             else: 
#                return f"Sorry, {name} Better luck next time. 😭😞"

#         game_result = decide_winner(player, computer)

#         print(game_result)     

#         nonlocal game_count
#         game_count += 1
        
#         print(f"\n Game count: {str(game_count)}")
#         print(f"{name}'s wins: {str(player_wins)}")

#         print(f"\n Play again, {name}")

#         while True:
#             playagain = input("\nY for yes \nQ for quit \n")
#             if playagain.lower() not in ["y", "q"]:
#                 continue
#             else:
#                 break

#         if playagain.lower() == "y":
#             return play_gn()
#         else:
#             print("\n🎉🎉🎉🎉🎉")
#             print("Thank you for playing!\n")
#             sys.exit(f"Bye {name}! 🙋‍♂️🙋‍♀️\n")

#     return play_gn

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

#     play = gn(args.name)
#     play()

        

        