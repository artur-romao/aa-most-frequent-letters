import os
import string
import random
from text_processing import treat_data, get_stopw_list

books = sorted([file for file in os.listdir("books") if file.endswith(".txt")]) # list with all the book files
stopw_files = sorted([file for file in os.listdir("stop-words") if file.endswith(".txt")]) # list with all the stop-words files

## DON'T FORGET TO CLOSE THE FILES

def frequent_count(letters, k):
    counts = {}
    frequent_letters = []
    for letter in letters:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
        
        if letter not in frequent_letters:
            if len(frequent_letters) < k:
                frequent_letters.append(letter)
            else:
                for freq_letter in frequent_letters:
                    counts[freq_letter] -= 1
                    if counts[freq_letter] == 0:
                        frequent_letters.remove(freq_letter)
                #frequent_letters.append(letter)
    
    return dict(sorted({letter: counts[letter] for letter in frequent_letters}.items(), key=lambda x: x[1], reverse=True))


for book in books:
    book_file = open("books/" + book, "r")
    stopw_file_name = stopw_files[books.index(book)] # get the stop-words file that corresponds to the book file (they're in the same order)
    stopw_file = open("stop-words/" + stopw_file_name, "r")
    stopwords = get_stopw_list(stopw_file)
    all_file_letters = []
    exact_counts = {}
    fixed_prob_counts = {} 
    for line in treat_data(book_file, stopwords):
        for letter in line:
            if letter in string.ascii_uppercase:
                all_file_letters.append(letter)
                if letter in exact_counts:
                    exact_counts[letter] += 1
                else:
                    exact_counts[letter] = 1
                if random.random() < 1 / 16:
                    if letter in fixed_prob_counts:
                        fixed_prob_counts[letter] += 1
                    else:
                        fixed_prob_counts[letter] = 1

    # sort the dictionaries by value and print them
    print("Letter counts for " + book + ":", dict(sorted(exact_counts.items(), key=lambda x: x[1], reverse=True)))
    print("Letter fixed prob counts for " + book + ":", dict(sorted(fixed_prob_counts.items(), key=lambda x: x[1], reverse=True)))
    print(frequent_count(all_file_letters, 10))
