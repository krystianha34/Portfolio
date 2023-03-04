# The program that reads the pickled files and calculates probability for each language.
# It computes the accuracy as a percentage of correctly classified instances in a test set. Using LangId.sol to
# determine correct classifications.

from nltk import word_tokenize
from nltk.util import ngrams
import pickle


# Computes the probability of a given language using LaPlace smoothing.
def compute_prob(test_text, unigram_dict, bigram_dict, v):
    # Tokenizes the line of text to be processed and turned into unigrams and bigrams.
    unigrams_test = word_tokenize(test_text)
    bigrams_test = list(ngrams(unigrams_test, 2))
    p_laplace = 1

    # Running the LaPlace smoothing here.
    for bigram in bigrams_test:
        # b is the bigram count
        b = bigram_dict[bigram] if bigram in bigram_dict else 0
        # u is the unigram count of the first word in the bigram
        u = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0

        p_laplace = p_laplace * ((b + 1) / (u + v))

    return p_laplace


if __name__ == '__main__':
    # Unpickling the files and assigns variables to them.
    with open("enuni.pickle", "rb") as handle:
        english_unigrams = pickle.load(handle)
    with open("enbi.pickle", "rb") as handle:
        english_bigrams = pickle.load(handle)

    with open("fruni.pickle", "rb") as handle:
        french_unigrams = pickle.load(handle)
    with open("frbi.pickle", "rb") as handle:
        french_bigrams = pickle.load(handle)

    with open("ituni.pickle", "rb") as handle:
        italian_unigrams = pickle.load(handle)
    with open("itbi.pickle", "rb") as handle:
        italian_bigrams = pickle.load(handle)

    # Opening the test file to determine what languages are which.
    with open("data/LangId.test", "r", encoding="utf8") as f:
        text = f.readlines()

    # Obtaining the total vocabulary count for all the language's unigrams.
    v = len(english_unigrams) + len(french_unigrams) + len(italian_unigrams)

    count = 0
    outfile = open("wordLangId.out", "w")

    # This for loop computes the probability for each language and puts the number into a variable. Then it finds the
    # largest value and determines which language it belongs to. Finally, it writes the current line count plus the
    # determined language to the "wordLangId.out" file.
    for line in text:
        count += 1
        # English
        enval = compute_prob(line, english_unigrams, english_bigrams, v)
        # French
        frval = compute_prob(line, french_unigrams, french_bigrams, v)
        # Italian
        itval = compute_prob(line, italian_unigrams, italian_bigrams, v)

        maxval = max(enval, frval, itval)

        # Checking each of the langauge values to figure out which one to use.
        if maxval == enval:
            outfile.writelines(str(count) + " English\n")
        elif maxval == frval:
            outfile.writelines(str(count) + " French\n")
        elif maxval == itval:
            outfile.writelines(str(count) + " Italian\n")

    outfile.close()

    # Opens the "wordLangId.out" file and the "LangId.sol" file to help determine accuracy.
    outfile = open("wordLangId.out", "r")
    solfile = open("data/LangId.sol", "r")

    # Gets all the lines within the file to be checked.
    sollines = solfile.readlines()
    correct = 0

    # This for loop goes through each line of the file and compares the results with test file.
    for line in sollines:
        # Tokenizes the solution and test file to be compared to each other.
        check = word_tokenize(outfile.readline())
        sol = word_tokenize(line)

        # Incrementing the correct amount by 1 if the languages are equal to each other.
        if check[1] == sol[1]:
            correct += 1
        else:
            # Outputs the line number for each incorrect guess.
            print("Incorrect Line: " + str(sol[0]))

    # Outputs the accuracy of the guesses to 2 decimal places.
    print("Accuracy: " + str(round(((correct / count) * 100), 2)) + "%")