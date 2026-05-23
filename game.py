import random

score = {"wins": 0, "losses": 0, "draws": 0}

def get_computer_choice():
    choices = ["stone", "paper", "scissors"]
    return random.choice(choices)

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "stone" and computer == "scissors") or \
         (player == "paper" and computer == "stone") or \
         (player == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"

def show_score():
    print(f"\nScore — Wins: {score['wins']} | Losses: {score['losses']} | Draws: {score['draws']}")

def play():
    print("🎮 Stone Paper Scissors!")
    print("------------------------")

    while True:
        player = input("\nEnter stone, paper or scissors (or 'quit' to exit): ").lower()

        if player == "quit":
            print("Thanks for playing! 👋")
            show_score()
            break

        if player not in ["stone", "paper", "scissors"]:
            print("Invalid choice! Try again.")
            continue

        computer = get_computer_choice()
        print(f"Computer chose: {computer}")

        result = get_winner(player, computer)

        if result == "win":
            print("🎉 You win!")
            score["wins"] += 1
        elif result == "lose":
            print("😞 You lose!")
            score["losses"] += 1
        else:
            print("🤝 It's a draw!")
            score["draws"] += 1

        show_score()

play()
