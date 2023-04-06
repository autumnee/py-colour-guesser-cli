from sty import bg, rs
import random

def generateRandomRGBColour() -> list:
    """
    Generate a list of 3 random 8-bit integers.

    :returns: A list of 3 valid and random 8-bit integers.
    """
    return list(random.choices(range(256), k=3))

def getUserInputs() -> list:
    """
    Generate user prompts to collect 3 valid 8-bit integers.

    :returns: The user input as a list of 3 8-bit integers
    """
    chosen_nums = list() 
    while len(chosen_nums) < 3:
        try:
            #TODO: Show what the current number is for (RGB)
            user_num = int(input("Input a number between 0 and 255: "))
            if(0 <= user_num <= 255):
                chosen_nums.append(user_num) # add the user num to the end of the list
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid number between 0 and 255.")
    return chosen_nums

#TODO: Make evaluation more interesting with different metrics!
def evaluateResult(actual: list, guessed:list):
    """
    Given a list of actual generated integers and the guesses from the user, 
    evaluates how close the guesses were to the correct numbers and prints a
    message.

    Both lists must have the same length.

    :param actual: The generated integers.
    :param guessed: The guessed integers from the user.
    """
    print(actual)
    print(guessed)
    cum_sum_list = list()
    for num in range(len(actual)):
        cum_sum_list.append(abs(actual[num] - guessed[num]))
    
    cum_sum = sum(cum_sum_list)
    # Three messages: One for "on the spot", one for "pretty close" and one for "yuck"
    if cum_sum == 0:
        print("YOU FOKING ROBOT")
    elif cum_sum <= 80:
        print("close... but not close enough!1")
    else:
        print("git gud n00b")
    print(cum_sum_list, cum_sum, sep='\n')
    return

def playRound():
    """
    Plays a single round of the colour guessing game.
    """
    color = generateRandomRGBColour()
    text = bg(color[0], color[1], color[2])+ "Guess my background colour!" + rs.bg
    print(text)
    game_values = getUserInputs()
    evaluateResult(color, game_values)

restart = True
while restart:
    playRound()
    playAgain = input("Play another round? (y/n): ")
    restart = playAgain == "y" or playAgain == "Y"