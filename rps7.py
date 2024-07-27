
import sys
import random
from enum import Enum

def rps(name):
    game_count = 0
    player_wins = 0
    python_wins = 0
    tie_game = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        nonlocal tie_game

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3   

        playerchoice = input(f"\n{name}, please enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name}, you choose {str(RPS(player)).replace('RPS.', " ")}.")
        print(f"Python choose {str(RPS(computer)).replace('RPS.', " ")}.\n")


        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            nonlocal tie_game
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, you win!"
            
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, you win!"
            
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, you win!"
                
            elif player == computer:
                tie_game += 1
                return "😲 Tie game!"
            
            else:
                python_wins += 1
                return f"🐍 Python wins!\nSorry, {name}...😞😓"

        game_result = decide_winner(player, computer)

        print(game_result)
        
        nonlocal game_count
        game_count += 1

        print(f"\n Game count: {str(game_count)}\n")
        print(f"{name}'s wins: {player_wins}")
        print(f"python_wins: {str(python_wins)}")
        print(f"tie_game: {str(tie_game)}")

        print(f"\n Play again, {name}?")

        while True:
            playagain =  input("\nY for yes \nQ for quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break    

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋🙋‍♂️🙋‍♀️")
            else:
                return

    return play_rps

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

    play = rps(args.name)
    play()