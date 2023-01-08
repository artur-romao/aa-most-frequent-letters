import os
import string
import random
from text_processing import treat_data, get_stopw_list

random.seed(98470)
books = sorted([file for file in os.listdir("books") if file.endswith(".txt")]) # list with all the book files
stopw_files = sorted([file for file in os.listdir("stop-words") if file.endswith(".txt")]) # list with all the stop-words files

## DON'T FORGET TO CLOSE THE FILES

for book in books:
    book_file = open("books/" + book, "r")
    stopw_file_name = stopw_files[books.index(book)] # get the stop-words file that corresponds to the book file (they're in the same order)
    stopw_file = open("stop-words/" + stopw_file_name, "r")
    stopwords = get_stopw_list(stopw_file)
    exact_counts = {}
    fixed_prob_counts = {}    
    for line in treat_data(book_file, stopwords):
        for letter in line:
            if letter in string.ascii_uppercase:
                if letter in exact_counts:
                    exact_counts[letter] += 1
                else:
                    exact_counts[letter] = 1
                if random.random() < 1 / 16:
                    if letter in fixed_prob_counts:
                        fixed_prob_counts[letter] += 1
                    else:
                        fixed_prob_counts[letter] = 1

    print("Letter counts for " + book + ":" + str(exact_counts))
    print("Letter fixed prob counts for " + book + ":" + str(fixed_prob_counts))
                
