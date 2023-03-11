## Web Crawler
### DESCRIPTION
Contains one python file as well as a document with a narrative detailing the creation of a knowledge base. 

This is a pretty basic web crawler. It begins with a given url and crawls through several websites, returning all relevant ones with some manual filtering thrown in. Then the top 15 urls are grabbed and text is extracted from them, and each url's text is put in to a file. Then each file gets cleaned up and put into a new file. Afterwards, the tf-idf for each file gets calculated and outputted to determine most relevant terms. More manual filtering done for the terms and the 10 most relevant ones are put into a dictionary to build a simple knowledge base. The cleantext files are looked through again and add sentences that contain any of the keys from the knowledge base. If a key is found in a sentence, then it get added to that key in the dictionary.

### HOW TO RUN
Download the main file and simply run the the [webcrawler.py](webcrawler.py) file to generate a knowledge base. 

NOTE: Be aware that serveral text files are created when running this program. 
