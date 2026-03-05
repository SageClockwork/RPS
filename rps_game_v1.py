import random

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):

    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item

            # check if the user response in the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item
        # print error if user does not enter a valid answer
        print(error)
        print()


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ***
    
To begin, chose the number of rounds (or press <enter> for 
infinite mode).
    
Then play against the computer. You need to chose R (rock), 
P (paper) or S (scissors).

The rules are as follows:
*   Paper beats rock
*   Rock beats scissors
*   Scissors beats paper

Press <xxx> to end the game at anytime.

Good Luck!
    """)


# checks for an integer more than 0 (allows <enter>)
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        # check for infinite mode
        if to_check == "":
            return "infinite"

        try:
            response = int(to_check)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def rps_compare(user_choice, comp_choice):

    if user_choice == comp_choice:
        round_result = "It's a tie"

    elif user_choice == "paper" and comp_choice == "rock":
        round_result = "You Win"
    elif user_choice == "rock" and comp_choice == "scissors":
        round_result = "You Win"
    elif user_choice == "scissors" and comp_choice == "paper":
        round_result = "You Win"

    else:
        round_result = "You Lose"

    return round_result


# main routine starts here
        
# Innitialise game variables
mode = "regular"
rounds_played = 0
rounds_tied = 0
rounds_lost = 0

rps_list = ["rock", "paper", "scissors", "xxx"]
game_history = []
            
            
print("🪨📄✂ Rock / Paper / Scissors Game ✂📄🪨")
print()
        

# ask the user if they want instructions (check they say yes / no)

want_instructions = string_checker("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()
        
# Ask the user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 5
        
# Game loop starts here
while rounds_played < num_rounds:

    # rounds headings
    if mode == "infinite":
        rounds_headings = f"\n=== Round {rounds_played + 1} (infinite mode) ==="
    else:
        rounds_headings = f"\n=== Round {rounds_played + 1} of {num_rounds} ==="

    print(rounds_headings)
    print()

    user_choice = string_checker("Choose: ", rps_list)

    if user_choice == "xxx":
        break

    comp_choice = random.choice(rps_list[:-1])
    print("Computer choice: ",comp_choice)

    result = rps_compare(user_choice, comp_choice)

    # adjust game lost / game tied counters and add results to game history
    if result == "It's a tie":
        rounds_tied = rounds_tied + 1

    elif result == "You Lose":
        rounds_lost = rounds_lost + 1


    print((f"{user_choice} vs {comp_choice}, {result}"))


    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1
     

# Game loop ends here
        
# Game history / statistics area

print()
print(f"""\n 🪨📄✂ Game History ✂📄🪨
      
Statistics:
      
Rounds played: {rounds_played}
Rounds tied: {rounds_tied}
Rounds lost: {rounds_lost}
Rounds won: {rounds_played - (rounds_tied + rounds_lost)}
Percentage won: %{(rounds_played - rounds_tied - rounds_lost) / rounds_played * 100}

      """)