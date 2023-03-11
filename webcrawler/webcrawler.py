# This is a pretty basic web crawler. It begins with a given url and crawls through several website, returning all
# relevant ones with some manual filtering thrown in. Then the top 15 urls are grabbed and text is extracted from them
# and each url's text is put in to a file. Then each file gets cleaned up and put into a new file. Afterwards, the
# tf-idf for each file gets calculated and outputted to determine most relevant terms. More manual filtering done for
# the terms and the 10 most relevant ones are put into a dictionary to build a simple knowledge base. The cleantext
# files are looked through again and add sentences that contain any of the keys from the knowledge base. If a key is
# found in a sentence, then it get added to that key in the dictionary.

import urllib
import urllib.request
import requests
import re
import math
import pickle
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup

# Defining the stop words to be used later in the program.
stop_words = set(stopwords.words("english"))


def get_links(starter_url):
    urls_list = []
    r = requests.get(starter_url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    counter = 1

    # Write urls to a file using beautiful soup to get the href tags.
    with open("urls.txt", "w") as f:
        f.write(starter_url + "\n")
        urls_list.append(starter_url)

        for link in soup.find_all("a"):
            if counter == 15:
                break
            link_str = str(link.get("href"))
            if "Kiryu" in link_str or "kiryu" in link_str \
                    or "yakuza" in link_str or "Yakuza" in link_str \
                    or "tekken" not in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    # print("MOD:", link_str)
                if "&" in link_str:
                    i = link_str.find("&")
                    link_str = link_str[:i]
                # A bunch of manual filtering of websites going on here, I feel like there is a better solution, but I
                # am not sure yet.
                if link_str.startswith("http") and "google" not in link_str \
                        and "twitter" not in link_str and "jp" not in link_str \
                        and "1up" not in link_str and "archive" not in link_str \
                        and "youtube" not in link_str and "wiki" not in link_str \
                        and "usgamer" not in link_str and "destructoid" not in link_str \
                        and "gematsu" not in link_str and "gamerbraves" not in link_str \
                        and "levelskip" not in link_str and "ww5" not in link_str:
                    f.write(link_str + "\n")
                    urls_list.append(link_str)
                    counter += 1

    #print("end of crawler")

    return urls_list


# A function that determines whether an element is visible or not.
def visible(element):
    if element.parent.name in ["style", "script", "[document]", "head", "title"]:
        return False
    elif re.match("<!--.*-->", str(element.encode("utf-8"))):
        return False
    return True


# Extracts the text from a given url and returns the entirety of it as a string.
def extract_text(url):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    data = soup.findAll(string=True)
    result = filter(visible, data)
    temp_list = list(result)
    temp_str = " ".join(temp_list)

    return temp_str


# Cleans up the text by removing tabs, newlines, and whitespace. It returns a list of sentences using the sentence
# tokenizer from nltk.
def clean_text(text):
    # Removing tabs and newlines
    fulltext = text.replace("\t\n", " ")
    # Removing whitespace
    text_chunks = [chunk for chunk in fulltext.splitlines() if not re.match(r"^\s*$", chunk)]
    # Converting to a single string
    cleantext = " ".join(text_chunks)
    # Using the NLTK sentence tokenizer to convert cleantext in to a list of sentences
    sent_list = sent_tokenize(cleantext)

    return sent_list


# Function responsible for creating the term frequency dictionary.
def create_tf_dict(text):
    # Tokenizing text for counting
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w.isalpha() and w not in stop_words]

    # Obtaining term frequencies.
    token_set = set(tokens)
    tf_dict = {t: tokens.count(t) for t in token_set}

    for t in tf_dict.keys():
        tf_dict[t] = tf_dict[t] / len(tokens)

    # A test loop to check weighted terms.
    """
    weighted_terms = sorted(tf_dict.items(), key=lambda x:x[1], reverse=True)
    count = 0

    for w in weighted_terms:
        if count > 30:
            break

        print(w[0])

        count += 1
    """

    return tf_dict


# Function for extracting important words in the text. It removes unnecessary punctuation and stopwords for one.
def extract_terms(text):
    # Removing punctuation and lower casing all text.
    fixedtext = re.sub(r"[^\w\s]", "", text)
    fixedtext = fixedtext.lower()

    # Tokenizing text to help remove stopwords
    tokens = word_tokenize(fixedtext)
    finaltext = ""

    # Simply removes stop words and combines the remaining ones into one string.
    for t in tokens:
        # Manually filtering out words that are not relevant to the topic
        if t not in stop_words and t != "best" and t != "new" and t != "wired" and t != "news" and t != "xbox" \
                and t != "engadget" and t != "k" and t != "ads" and t != "mario" and t != "view":
            finaltext = finaltext + " " + t

    return create_tf_dict(finaltext)


# Function that creates the tf_idf dictionary to be used for finding important terms throughout all the sites.
def create_tfidf(tf, idf):
    tf_idf = {}

    # Calculating the tf_idf here
    for t in tf.keys():
        tf_idf[t] = tf[t] * idf[t]

    return tf_idf


# Main runner function.
if __name__ == '__main__':
    # Starter url
    start_url = "https://en.wikipedia.org/wiki/Yakuza_(franchise)"
    # Obtaining the first 15 links including the starter that is relevant to the topic.
    url_list = get_links(start_url)

    # Extracting text and writing to a file
    for link in url_list:
        filename = "url" + str(url_list.index(link) + 1) + ".txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(extract_text(link))

    # Cleaning up the text files
    for i in url_list:
        # Reading in the url text files to be cleaned up.
        filename = "url" + str(url_list.index(i) + 1) + ".txt"
        with open(filename, "r", encoding="utf-8") as f:
            filetext = f.read()
            sentence_list = clean_text(filetext)

        # Writing all the cleaned text to new files to be used later.
        newfilename = "cleantext" + str(url_list.index(i) + 1) + ".txt"
        with open(newfilename, "w", encoding="utf-8") as f:
            for sent in sentence_list:
                f.write(sent + "\n")

    total_vocab = []
    total_dict = []

    # Determining important terms
    for i in url_list:
        # Going through the clean text to determine term frequency.
        filename = "cleantext" + str(url_list.index(i) + 1) + ".txt"
        with open(filename, "r", encoding="utf-8") as f:
            filetext = f.read()

            # Getting the term frequency here.
            tfdict = extract_terms(filetext)

            # Assigning each term frequency to a dictionary to be used for finding the idf.
            if url_list.index(i) == 0:
                vocab = set(tfdict.keys())

            vocab = vocab.union(set(tfdict.keys()))
            total_dict.append(tfdict)
            total_vocab.append(tfdict.keys())

    idf_dict = {}

    # Creating the idf dictionary to be used for the tf-idf
    for term in vocab:
        temp = ["x" for voc in total_vocab if term in voc]
        idf_dict[term] = math.log((1 + 15) / (1 + len(temp)))

    # Creating the tf-idf's for all the text files
    for x in total_dict:
        create_tfidf(total_dict[total_dict.index(x)], idf_dict)
        # Sorting the terms by their weight for determining top 10 terms
        term_weights = sorted(total_dict[total_dict.index(x)].items(), key=lambda x: x[1], reverse=True)
        # Printing out the top 40 terms for each file
        print("weighted terms " + str(total_dict.index(x) + 1) + ": ", term_weights[:40])

    # Based on the output of the above, I determined the following 10 terms based on my knowledge and ranking:
    # 1. Yakuza 2. Gaming 3. Series 4. Kiryu 5. Kamurocho 6. Dragon 7. Action 8. Japanese 9. Nagoshi 10. Sega

    # Here I am making a terms dictionary for each of the above terms. They will each contain a list of sentences taken
    # from the cleaned up text files.
    terms_dict = {"Yakuza": [], "gaming": [], "series": [], "Kiryu": [], "Kamurocho": [],
                  "dragon": [], "action": [], "Japanese": [], "Nagoshi": [], "Sega": []}

    # Building a knowledge base here by going through the clean text files and assigning sentences to the terms_dict
    for i in url_list:
        filename = "cleantext" + str(url_list.index(i) + 1) + ".txt"
        with open(filename, "r", encoding="utf-8") as f:
            filetext = f.read()
            sent_list = sent_tokenize(filetext)

            # Iterating through the keys in the dictionary
            for key in terms_dict:
                # Iterating through the sentences in sent_list
                for sent in sent_list:
                    # If a key is found in the sentence, then it is added to the knowledge base.
                    if key in sent:
                        terms_dict[key].append(sent)

    # Pickling the dictionary for ease of use elsewhere.
    pickle.dump(terms_dict, open("terms.pickle", "wb"))
