import random

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

def get_winner(user, comp):
    if user == comp:
        return "Tie"
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        return "User"
    else:
        return "Computer"

while True:
    print("\n--- Rock Paper Scissors ---")
    user = input("Choose rock, paper, or scissors (or 'exit' to quit): ").lower()
    if user == "exit":
        break
    if user not in choices:
        print("Invalid choice.")
        continue
    computer = random.choice(choices)
    winner = get_winner(user, computer)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")
    if winner == "User":
        print("🎉 You win!")
        user_score += 1
    elif winner == "Computer":
        print("💻 Computer wins!")
        computer_score += 1
    else:
        print("😐 It's a tie!")

    print(f"Score -> You: {user_score}, Computer: {computer_score}")
