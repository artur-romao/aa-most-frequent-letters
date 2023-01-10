import os
import string
import random
from text_processing import treat_data, get_stopw_list

books = sorted([file for file in os.listdir("books") if file.endswith(".txt")]) # list with all the book files
stopw_files = sorted([file for file in os.listdir("stop-words") if file.endswith(".txt")]) # list with all the stop-words files


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
    # threshold = sum([counts[letter] for letter in frequent_letters]) / k # add if counts[letter] > threshold in line below
    return dict(sorted({letter: counts[letter] for letter in frequent_letters}.items(), key=lambda x: x[1], reverse=True))
    

languages = [book.replace("oliver_twist_", "").replace(".txt", "") for book in books]
all_files_letters = {language : [] for language in languages} # initialize a list for each book to store every character
all_counts = {language : {} for language in languages} # initialize a dictionary for each book to store the counts of each letter
n_tests = 30
for book in books:
    language = book.replace("oliver_twist_", "").replace(".txt", "")
    flag = False # this flag is used to compute the exact_counts only once for each book
    fixed_prob_absolute_errors = [] 
    fixed_prob_relative_errors = []
    avg_frequent_letters = {letter : 0 for letter in string.ascii_uppercase}
    exact_counts = {}
    for i in range(n_tests): # run 30 tests to get a better estimate of the errors
        book_file = open("books/" + book, "r")
        stopw_file_name = stopw_files[books.index(book)] # get the stop-words file that corresponds to the book file (they're in the same order)
        stopw_file = open("stop-words/" + stopw_file_name, "r")
        stopwords = get_stopw_list(stopw_file)
        fixed_prob_counts = {} 
        for line in treat_data(book_file, stopwords):
            for letter in line:
                if letter in string.ascii_uppercase:
                    if not flag: # flag here so we only compute exact counts once (in the first iteraction)
                        all_files_letters[language].append(letter)
                        if letter in exact_counts:
                            exact_counts[letter] += 1
                        else:
                            exact_counts[letter] = 1
                    if random.random() < 1 / 16:
                        if letter in fixed_prob_counts:
                            fixed_prob_counts[letter] += 1
                        else:
                            fixed_prob_counts[letter] = 1
        flag = True
        all_counts[language] = exact_counts
        for letter, count in fixed_prob_counts.items():
            avg_frequent_letters[letter] += count
            absolute_error = abs(count - exact_counts[letter])
            relative_error = absolute_error / exact_counts[letter]
            fixed_prob_absolute_errors.append(absolute_error)
            fixed_prob_relative_errors.append(relative_error)
        
        book_file.close()
        stopw_file.close()

    exact_counts = dict(sorted(exact_counts.items(), key=lambda x: x[1], reverse=True))
    with open("results/exact_count_" + book, "w") as f:
        f.write("order letter count\n")
        for i, (letter, count) in enumerate(exact_counts.items()):
            f.write(str(i + 1) + " " + letter + " " + str(count) + "\n")
        f.close()

    # compute the average frequent letters
    avg_frequent_letters = {letter: avg_frequent_letters[letter] / n_tests for letter in avg_frequent_letters}
    avg_frequent_letters = dict(sorted(avg_frequent_letters.items(), key=lambda x: x[1], reverse=True))
    
    with open("results/fixed_prob_" + book, "w") as f:
        f.write("order letter count\n")
        for i, (letter, count) in enumerate(avg_frequent_letters.items()):
            f.write(str(i + 1) + " " + letter + " " + str(round(count, 2)) + "\n")
        f.close()

    avg_absolute_error = sum(fixed_prob_absolute_errors) / len(fixed_prob_absolute_errors)
    min_absolute_error = min(fixed_prob_absolute_errors)
    max_absolute_error = max(fixed_prob_absolute_errors)
    
    avg_relative_error = sum(fixed_prob_relative_errors) / len(fixed_prob_relative_errors)
    min_relative_error = min(fixed_prob_relative_errors)
    max_relative_error = max(fixed_prob_relative_errors)

    print("STATISTICS FOR FIXED PROBABILITY 1/16 " + book + ":")
    print(f"Average absolute error: {avg_absolute_error:.2f}")
    print(f"Minimum absolute error: {min_absolute_error}")
    print(f"Maximum absolute error: {max_absolute_error}")
    print(f"Average relative error: {avg_relative_error:.2f}")
    print(f"Minimum relative error: {min_relative_error:.2f}")
    print(f"Maximum relative error: {max_relative_error:.2f}\n\n\n")


for language in all_files_letters:
    with open("results/frequent_count_oliver_twist_" + language + ".txt", "w") as f:
        f.write("k order letter count\n")
        for k in [3, 5, 10]:
            absolute_errors = []
            relative_errors = []
            estimated_count = frequent_count(all_files_letters[language], k)
            for i, (letter, count) in enumerate(estimated_count.items()):
                f.write(str(k) + " " + str(i + 1) + " " + letter + " " + str(count) + "\n")
                exact_count = all_counts[language][letter] # get the exact count for the letter in the book
                absolute_error = abs(count - exact_count)
                relative_error = absolute_error / exact_count
                absolute_errors.append(absolute_error)
                relative_errors.append(relative_error)
            
            avg_absolute_error = sum(absolute_errors) / len(absolute_errors)
            min_absolute_error = min(absolute_errors)
            max_absolute_error = max(absolute_errors)
            
            avg_relative_error = sum(relative_errors) / len(relative_errors)
            min_relative_error = min(relative_errors)
            max_relative_error = max(relative_errors)
            
            print("STATISTICS FOR FREQUENT COUNT (k = " + str(k) + ") oliver_twist_" + language + ".txt:")
            print(f"Average absolute error: {avg_absolute_error:.2f}")
            print(f"Minimum absolute error: {min_absolute_error}")
            print(f"Maximum absolute error: {max_absolute_error}")
            print(f"Average relative error: {avg_relative_error:.2f}")
            print(f"Minimum relative error: {min_relative_error:.2f}")
            print(f"Maximum relative error: {max_relative_error:.2f}\n\n\n")

    f.close()
