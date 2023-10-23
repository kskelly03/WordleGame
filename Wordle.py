# Tulane University, CMPS 1500, Spring 2023
#
# STUDENTS MUST FILL IN BELOW
#
# Student name: Kevin Skelly
# Student email address: kskelly@tulane.edu
#
# Collaborators: Garrett Gilliom

# NOTE: you must write your own code. You may discuss the assignment with 
#       professors, TAs, other students, or family members. But you MUST
#       list anyone you collaborated with in the space above.

# ALSO NOTE: You must add comments which explain how your solution works.
#            If you do not do this, your solution will not receive credit.

import random

from WordleWordlist import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_ROWS, N_COLS
from WordleGraphics import CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR
# solution = random.choice(FIVE_LETTER_WORDS)
solution = "stink"
def enter_action(guessedword):
    """ This function is called any time the enter button
    is clicked/typed in the game. guessedword is the player's most
    recent guess which needs to be checked.
    """

    # Milestone 0.5: put test code here to display
    # y = 0
    # for x in solution:
    #        gw.set_square_letter(0, y, x)
    #        y +=1

    # also show a message on the gameboard indicating that this is for milestone 1
    # gw.show_message("This is for milestone 1") # replace this
    # end milestone 0

    # Milestones 1+: put code below here (make sure it is indented)
    if guessedword.lower() in FIVE_LETTER_WORDS:  # Lowercase the word to compare it with the 5 letter word dictionary
        y = 0  # Set our column variable to zero before the for loop runs
        for x in guessedword:  # For loop to run through each letter in the guessed word
            gw.set_square_letter(gw.get_current_row(), y, x)
            if x.lower() in solution[y]:  # Letter must be lowercased to match the solution, and then compared with
                # the letter in the solution at the same index
                gw.set_square_color(gw.get_current_row(), y, CORRECT_COLOR)  # Fill the box with the "correct" color
                # if the letter is at its proper index
                gw.set_key_color(x, CORRECT_COLOR)
            elif x.lower() in solution:  # Now the letter is compared with the whole solution word.
                gw.set_square_color(gw.get_current_row(), y, PRESENT_COLOR)  # Fill the box with the "present" color
                # if the letter is present but not at the correct index
                if not gw.get_key_color(x) == CORRECT_COLOR:
                    gw.set_key_color(x, PRESENT_COLOR)
            else:
                gw.set_square_color(gw.get_current_row(), y, MISSING_COLOR)  # Fill the box with the "missing" color
                # if the letter is not present
                gw.set_key_color(x, MISSING_COLOR)
            y += 1  # Increase the column variable by 1
        if guessedword.lower() in solution:
            gw.show_message("You win!")
        else:
            gw.set_current_row(gw.get_current_row() + 1)
    else:
        gw.show_message("Not in wordlist")  # If the word isn't in the word list, print a message and do not incr. row
    print(solution)


# Students: do not change anything below here
gw = WordleGWindow()
gw.add_enter_listener(enter_action)
