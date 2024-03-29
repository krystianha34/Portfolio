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

## [Web Crawler](webcrawler)
### DESCRIPTION
Contains one python file as well as a document with a narrative detailing the creation of a knowledge base. 

This is a pretty basic web crawler. It begins with a given url and crawls through several websites, returning all relevant ones with some manual filtering thrown in. Then the top 15 urls are grabbed and text is extracted from them, and each url's text is put in to a file. Then each file gets cleaned up and put into a new file. Afterwards, the tf-idf for each file gets calculated and outputted to determine most relevant terms. More manual filtering done for the terms and the 10 most relevant ones are put into a dictionary to build a simple knowledge base. The cleantext files are looked through again and add sentences that contain any of the keys from the knowledge base. If a key is found in a sentence, then it get added to that key in the dictionary.

### HOW TO RUN
Download the main file and simply run the the [webcrawler.py](webcrawler/webcrawler.py) file to generate a knowledge base. 

NOTE: Be aware that serveral text files are created when running this program. 

## [Text Classification](textclassification.ipynb)
### DESCRIPTION
A study on text classification through the use of Naive Bayes, Logistic Regression, and Neural Networks. 

### WHAT I LEARNED
Each of the 3 machine learning techniques had their own strong points, but some certainly outshine others. Naive Bayes is simpler and tends to produce a lower accuracy compared to the other two. Logistic Regression is a little more complicated and produces a higher accuracy than Naive Bayes. And finally, Neural Networks are capable of producing the highest accuracy. But they are dependent on having a large amount of nodes to obtain that accuracy. If I were working with small data sets, I'd consider using Naive Bayes or Logistic Regression. And if I were working with a large data set, then neural networks would be my ML of choice. 

## [ACL Paper Summary](portfolio_acl_paper.pdf)
### Description
A summary of an ACL paper that I read for my class. It covers the idea that prompt-based models may be clueless as they rely more on superficial cues within datasets and do not perform well with generalization. 

Link to the paper: https://aclanthology.org/2022.acl-long.166/

## [Text Classification 2](textclassification2.ipynb)
### DESCRIPTION
Another study on text classification using deep learning techniques such as a sequential approach, RNN, and an embedded approach.

### WHAT I LEARNED
From the three different methods tested, those being a sequential model, RNN, and an embedded approach, the sequential model scored the highest with RNN behind it and the embedded approach at the lowest. The sequential model did not take too much time to compile and it gave a good accuracy over the 10 epochs tested. RNN took about an hour to compile which I believe is due to the amount of layers put on the model. However, I do not believe its accuracy would be as high as a result. And finally, the embedded approach did not provide a good accuracy compared to the other two. So for me, the sequential model would be the preffered option when it comes to text classification.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SUMMARY
Over the course of the semester, I learned quite a lot about Natural Language Processing and how it is used in plenty of modern programs today. From building simple guessing games all the way up to a chatbot, there was a lot covered. For the amount of material covered, I feel like the class was well paced and taught by example and not just tests. By doing these assignments, I can fully delve in to the kind of NLP problems that are being faced today. It is certainly an exciting field of study and I am interested to see how it develops in the future. I do not have any plans for future personal projects at the moment as I have other things to take care of in the meantime. As the field grows and changes, I will need to stay in touch with the field in order to not fall behind since NLP is looking to be quite impactful in the future. As I currently have a place of employment, I do not have immediate interest in NLP related employment opportunites. But I will definitely keep them in mind for the future.  
