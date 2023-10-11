import random

def get_user_choice():
    print("Choose rock, paper, or scissors:")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors:")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "You lose!"

def play_again():
    print("Do you want to play again? (yes/no)")
    return input().lower().startswith('y')

def main():
    score = {'user': 0, 'computer': 0}
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}, the computer chose {computer_choice}.")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            score['user'] += 1
        elif result == "You lose!":
            score['computer'] += 1
        print(f"Score: You {score['user']}, Computer {score['computer']}")
        if not play_again():
            break

if __name__ == "__main__":
    main()
