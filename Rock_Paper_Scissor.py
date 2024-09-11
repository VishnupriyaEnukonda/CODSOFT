import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_round():
    print("Choose Rock, Paper, or Scissors:")
    user_choice = input("Your choice: ").lower()
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return None, None
    
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    result = determine_winner(user_choice, computer_choice)
    print(result)
    
    return result, computer_choice

def game():
    user_score = 0
    computer_score = 0

    while True:
        print("\n--- Rock, Paper, Scissors Game ---")
        result, computer_choice = play_round()
        
        if result is not None:
            if "win" in result:
                user_score += 1
            elif "lose" in result:
                computer_score += 1

            print(f"\nCurrent Score: You: {user_score} | Computer: {computer_score}")
        
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("\n--- Final Score ---")
    print(f"You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    game()
