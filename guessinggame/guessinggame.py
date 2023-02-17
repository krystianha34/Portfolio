# Guessing Game by Krystian Ayala
#
# This is a guessing game with basic functionality. The main thing about this program is extracting nouns from any piece
# of given text and using the 50 most common nouns as the words being guessed. The given text is preprocessed using the
# NLTK toolkit. For the guessing game, it is simplistic, mainly to showcase the ability of NLTK. The player starts with
# 5 points, and they get 1 point for guessing correctly and lose a point for an incorrect guess. If their points go into
# the negatives, then the game is over. If the word is completely guessed, then a new word is given to guess. The
# character "!" can be inputted to exit out of the game and end the program.

import nltk
import sys
import random

from nltk.tokenize import word_tokenize
from nltk.text import Text
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import FreqDist


def process_text(text):
    # Removing new line characters and replacing with blank spaces.
    processed_text = text.replace("\n", " ")
    # Tokenizing the text for easy filtering.
    tokens = word_tokenize(processed_text)

    # Getting rid of punctuation and numbers, also formatting to lower case.
    tokens = [t.lower() for t in tokens if t.isalpha() and t not in stopwords.words("english") and t in tokens if
              len(t) > 5]
    # Obtaining all the tokens in the text.
    text_const = Text(tokens)
    # Obtaining the unique number of tokens in the text.
    text_set = set(text_const)

    # Outputting the lexical diversity of the text after preprocessing formatted to 2 decimal places.
    print("Lexical diversity: %.2f" % (len(text_set) / len(text_const)))

    # Getting the lemmas
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]
    # Making the lemmas unique
    lemmas_unique = list(set(lemmas))
    # Creating the tags for the unique lemmas and outputting the first 20
    tags = nltk.pos_tag(lemmas_unique)
    print("\nThe first 20 tagged unique lemmas:", tags[:20])
    # Making a list of most common nouns in the document.
    common_nouns = [word for word, pos in nltk.pos_tag(lemmas) if pos.startswith("NN")]
    common_nouns = FreqDist(common_nouns)
    common_nouns = common_nouns.most_common(50)

    # Creating a new list of unique lemmas that consist only of nouns.
    nouns = [word for word, pos in tags if pos.startswith("NN")]
    # Outputting the number of tokens in the file.
    print("The number of tokens in the file:", len(text_const))
    # Outputting the number of nouns in the file.
    print("The number of nouns in the file:", len(nouns), "\n")

    return text_const, nouns, common_nouns


# Main function for running the game.
def driver(text_file):
    with open(text_file, "r") as f:
        text = f.read()
    # Processing text and returning 3 variables: a string called 'text', a list called 'nouns', and
    # another list called 'common_nouns'
    text, nouns, common_nouns = process_text(text)
    # This is a conversion of the common_nouns list into a dictionary.
    noun_dict = {common_nouns[i][0]: common_nouns[i][1] for i in range(0, len(common_nouns), 2)}
    # Prints out the 50 most common nouns in the text.
    print("50 most common words:")
    for pos in sorted(noun_dict, key=noun_dict.get, reverse=True):
        print(pos, ':', noun_dict[pos])

    # Infinite loop for the guessing game. The game completely ends when points are out, but will continue as long as
    # the player still has points (including 0).
    while 1 > 0:
        # Starts the guessing game.
        print("\nLet's play a word guessing game!")
        # A random key is picked from the dictionary to be used
        word = random.choice(list(noun_dict.keys()))
        # This print statement is here for debugging purposes.
        print(word)
        # Initializing points to 5.
        points = 5
        # Making a list of spaces that are the same length as the chosen word.
        spaces = ['_'] * len(word)

        # Second loop which functions as the game itself. It will exit when points are negative or user inputs "!"
        # It will break out of the loop if the word is guessed correctly and a new word will be chosen, restarting the
        # game while remembering its points.
        while points >= 0:
            # Prints the "_" chars in a clean fashion.
            print(*spaces)
            # Prompts the user to guess a letter.
            guess = input("Guess a letter: ")

            # Breaks out of the loop if the player inputs "!"
            if guess == "!":
                print("The game is over, ending session.")
                return

            # This if statement is responsible for updating the spaces list if the guess is contained in the word.
            if guess in word:
                word, spaces = find_letter_spot(guess, word, spaces)
                points += 1
                print("Right! Score is ", points)
            else:
                points -= 1

                # A check to determine if points have gone negative, exiting the game if so.
                if points < 0:
                    print("Points have run out, try again.")
                    return

                print("Sorry, guess again. Score is ", points)

            # If statement to check if the word has been solved. Breaks out of the loop if so and starts a new game.
            if win_valid(spaces) == 1:
                print("You solved it!\n")
                break

        print("Current score: ", points)


# Function for finding the correct spot for a word and replacing the "_" with its respective letter.
def find_letter_spot(guess, word, spaces):
    index = -2

    # A simple while loop that exits if index is set to -1.
    while index != -1:
        if guess in word:
            # Finds the index of the char(s) needing to be replaced.
            index = word.find(guess)
            removed_char = "*"
            # Replacing the "_" with the guessed letter.
            word = word[:index] + removed_char + word[index+1:]
            spaces[index] = guess
        else:
            index = -1

    return word, spaces


# A simple check to determine if all the spaces have been filled and if the player has won the game.
def win_valid(spaces):
    # Checks if there's any remaining spaces in the list.
    for i in range(0, len(spaces)):
        if spaces[i] == "_":
            return -1
    return 1


# Main function that starts the game.
if __name__ == "__main__":
    # file name
    if len(sys.argv) > 1:
        # Obtains file from sys.arg, any .txt file can be used for this.
        arg_input = sys.argv[1]
        print("Input files: ", arg_input)
        # The driver function starts the game.
        driver(arg_input)
    else:
        print("File name missing")
    print("\nProgram ended")
