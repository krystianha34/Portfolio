# Portfolio
My portfolio of various projects.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Introduction to NLP](Overview_of_NLP.pdf)

This is an introductory document for my class, Human Language Technologies, in which I discuss Natural Language Processing.

## [Data Processor](dataprocessor)

### DESCRIPTION
The two files to run this program are located here: 
[Data Processor](dataprocessor/dataprocessor.py) and [Data File](dataprocessor/data.csv)

A simple program in Python to take an input file using sysarg and correct errors in formatting. It will prompt the user to fix the mistakes if any, then adds these values into a dictionary. 

The example uses sample employee information. Given a last and first name, middle initial, employee id, and a phone number. They are formatted in a uniform way and if there's an error, then the user is prompted to fix it by inputting a new value. 

Finally, the information is put into a dictionary and turned into a .pickle file. The program reads the .pickle file back and displays the employee information so the user can confirm everything is correct. 

### HOW TO RUN
Download both the files and simply run the program with a parameter for the file location of the data.csv file

### STRENGTHS / WEAKNESSES OF PYTHON FOR TEXT PROCESSING
I would say that Python is incredibly useful for processing text and filtering until a desired outcome can be achieved. There is a lot of methods and versatility with strings as well. I am looking forward to seeing how far this can go, especially with Natural Language Processing. 

### WHAT I LEARNED
Since this was my first actual Python program I wrote, I learned quite a lot. Having been introduced to what Python is and how best to use it, I was looking forward to trying it out. This program helped me to realize the potential of Python when it comes to processing large amounts of data and formatting if needed.

## [Guessing Game](guessinggame)
### DESCRIPTION
The two files to run this program are located here: 
[Guessing Game](guessinggame/guessinggame.py) and [Sample Text File](guessinggame/anat19.txt)

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

## [WordNet](wordnet.ipynb)
### DESCRIPTION
Simply a study on WordNet exploring its uses and whatnot. 

### WHAT I LEARNED
Like my intro to NLTK with the [guessing game](guessinggame/guessinggame.py), I learned a lot more about processing text and how to make use of the many tools within WordNet. Continuing my studies in Python and its uses, I can turn it into a powerful tool for automating collecting and using of large amounts of data.

## [N-grams](n-grams)
### DESCRIPTION
Contains two python files as well as a folder for the data and a narrative about n-grams. Essentially determines the probability of a certain language given some sample text. It creates a file with these guesses that are then compared to a solution file. An accuracy indicator is outputted to the console afterwards. 

### HOW TO RUN
Download all the files and simply run the the [process.py](n-grams/process.py) file to process the given data within the [data](n-grams/data) folder. Then run the [runner.py](n-grams/runner.py) file after to determine accuracy of the probabilities. 

### WHAT I LEARNED
I would say this is my first real run with training a language model in Python. N-grams appear to be quite useful from what I can see so far and I am looking forward to implementing them more as I continue to code. 

## [Sentence Parsing](sentenceparsing.pdf)
### DESCRIPTION
A .pdf file of written parses for a given sentence with some brief descriptions to aid in understanding.

### PROS / CONS OF EACH PARSE TYPE
I want to say the PSG parse tree is my preferred option when it comes to parsing sentences. I prefer the tree and it is much more readable than the other two in my opinion. Although, I feel it is lacking when it comes to accurately describing the words and their meanings. The dependency parse looks the most detailed and comes with a large number of definitions for words and how they influence others. But I am not a fan of the organization and it can feel slightly cryptic trying to read everything. Finally, SRL parse trees are about in the middle. They are more readable than a dependency parse, but not as much as a PSG parse tree. The arguments are easy to understand and see how they influence other words. 
