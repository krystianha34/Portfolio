# Guessing Game
### DESCRIPTION
The two files to run this program are located here: 
[Guessing Game](guessinggame.py) and [Sample Text File](anat19.txt)

A program in Python to take an input file using sysarg and process the text. It retrieves the 50 most common nouns in the given text and picks a random one to start a guessing game. 

The example is taken from an anatomy textbook. NLTK is used to filter the 50 most common nouns within the text. Then a word from that list is randomly picked to use in the guessing game. 

The guessing game starts the player with five points and one point is given for each correct guess. One point is lost for each incorrect guess. If the total points go below zero, then the game ends and the program exits. If the player guesses the word correctly, then a new word is given to guess.

At any moment in the program, the player can input "!" to end the game and program.

### HOW TO RUN
Download both the files and simply run the program with a parameter for the file location of the anat19.txt file

### STRENGTHS / WEAKNESSES OF PYTHON FOR TEXT PROCESSING
Once again, Python has shown its usefulness in filtering through a large amount of text to retrieve specific types of words. NLTK has a plethora of options for finding exactly what you need for a given situation.

### WHAT I LEARNED
Being my second Python program I wrote. I learned much more about the benefits of NLTK to process large amounts of text and retrieve what you need. As I continue to make more Python programs, NLTK will be a valuable tool as I make more. 
