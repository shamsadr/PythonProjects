# This is a very basic rock, paper, scissors game.
# Here, the user enters 1, 2, or 3 to
# denote their choice of rock, paper, or scissors
# and plays against the computer.

# Import Libraries
import random

# This function prompts the user for an input
# and gets an user input to play the game

def get_player_choice():
    print("\nPlease select from the following: ")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")

# Input Validation

    while True:
        try:
            player_choice = int(input("Enter your choice (1/2/3): "))
            if player_choice in [1, 2, 3]:
                return player_choice
            else:
                print("Invalid input, please enter a number between 1, 2,or 3")
        except ValueError:
            print("Enter an integer between 1, 2, or 3")

# This function converts the integer selection by the player
# into a string and feeds it to the program
def move_to_string(move):
    moves = {1 : 'Rock', 2 : 'Paper', 3 : 'Scissors'}
    return(moves[move])

# This function determines the winner of a round by
# using the logic provided
def determine_winner(player, computer):
    if player == computer:
        print("It\'s a tie.")
    elif (player == 1 and computer == 3) or \
         (player == 3 and computer == 2) or \
         (player == 2 and computer == 1):
             print("Player Wins!")
    else:
         print("Computer Wins!")

# Main Function

def play_game():

    player_score = 0
    computer_score = 0
    rounds = 3

    # Loop to get the result of the rounds
    for round in range(1, rounds + 1):
        print(f"\n-----Round {round}-----")

        player_choice = get_player_choice()
        computer_choice = random.randint(1, 3)

        print(f"You chose {move_to_string(player_choice)}")
        print(f"The computer chose {move_to_string(computer_choice)}")

        result = determine_winner(player_choice, computer_choice)

        if result == "Player Wins!":
            player_score += 1
        elif result == "Computer Wins!":
            computer_score += 1
        else:
            print("This round ends in a tie!")

        print(f"Score --> You: {player_score}, Computer: {computer_score}")

    # Announcing the overall winner

    print("\n-----Final Results-----")
    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif computer_score > player_score:
        print("The Computer Wins!")
    else:
        print("It's a tie!")

play_game()
