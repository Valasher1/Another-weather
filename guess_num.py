import random
import sys


def gn(name='PlayerOne'):
    game_count    = 0
    player_wins   = 0

    def play_gn():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(f"\n{name}, guess which number I'm thinking of ... 1, 2, or 3: \n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_gn()

        computerchoice = random.choice("123")

        print(f"\n{name}, you choose {playerchoice}.")
        print(f"I was thinking about the number {computerchoice}.\n")

        player = int(playerchoice)
        computer = int(computerchoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you win!\n"

            else: 
               return f"Sorry, {name} Better luck next time. 😭😞"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f" Game count: {str(game_count)}")
        print(f"\n{name}'s wins: {str(player_wins)}")
        print(f"\nYour winning percentage: {player_wins/game_count:.2%}")

        print(f"\n Play again, {name}")

        while True:
            playagain = input("\nY for yes \nQ for quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gn()
        else:
            print("\n🎉🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye {name}! 👋🙋‍♂️🙋‍♀️")
            else:
                return

    return play_gn

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

    run_gn = gn(args.name)
    run_gn()

        
     