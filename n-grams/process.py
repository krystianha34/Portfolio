# Python file primarily for processing the text of 3 given files and pickling 2 dictionaries that came from a text
# processing function. 

from nltk import word_tokenize
from nltk.util import ngrams
import pickle


# Function responsible for removing newlines and tokens the words. Then it turns those tokens into unigrams and bigrams.
# Finally, it makes the unigrams and bigrams into dictionaries and returns those.
def process_text(text_file):
    # Reading the file with UTF-8 encoding to support non-English languages.
    with open(text_file, "r", encoding="utf8") as f:
        text = f.read()
    # Replacing new lines with blank spaces in the text.
    text = text.replace("\n", " ")
    # Creating the unigrams by tokenizing the text.
    unigrams = word_tokenize(text)
    # Making the bigrams using ngrams from nltk
    bigrams = list(ngrams(unigrams, 2))
    # Creating dictionaries for both the unigrams and bigrams.
    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}

    # Returning the two dictionaries.
    return unigram_dict, bigram_dict


# Main file for calling the process_text function for each of the 3 languages and then pickling the dictionaries to be
# used in the runner.py file
if __name__ == '__main__':
    # Processing the English file into 2 separate pickles for unigrams and bigrams.
    english_unigrams, english_bigrams = process_text("data/LangId.train.English")
    with open("enuni.pickle", "wb") as handle:
        pickle.dump(english_unigrams, handle)
    with open("enbi.pickle", "wb") as handle:
        pickle.dump(english_bigrams, handle)

    # Processing the French file into 2 separate pickles for unigrams and bigrams.
    french_unigrams, french_bigrams = process_text("data/LangId.train.French")
    with open("fruni.pickle", "wb") as handle:
        pickle.dump(french_unigrams, handle)
    with open("frbi.pickle", "wb") as handle:
        pickle.dump(french_bigrams, handle)

    # Processing the Italian file into 2 separate pickles for unigrams and bigrams.
    italian_unigrams, italian_bigrams = process_text("data/LangId.train.Italian")
    with open("ituni.pickle", "wb") as handle:
        pickle.dump(italian_unigrams, handle)
    with open("itbi.pickle", "wb") as handle:
        pickle.dump(italian_bigrams, handle)
