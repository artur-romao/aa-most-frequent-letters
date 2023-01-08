import re

def treat_data(book_f, stopwords):
    header_removed = False  # flag to track if the header has been removed
    for line in book_f.readlines():
        if line.strip() == "*** END OF THIS PROJECT GUTENBERG EBOOK OLIVER TWIST ***": # stop the reading once the footer is detected
            break
        elif header_removed:  # start yielding lines once the header has been removed
            line = capitalize_line(line)
            line = filter_stopwords(line, stopwords)
            yield line
        elif line.strip() == "*** START OF THE PROJECT GUTENBERG EBOOK OLIVER TWIST ***":
            header_removed = True  # start the flag once the header is detected

def filter_stopwords(line, stopwords):
    new_line = ""
    for word in line.split():
        if word not in stopwords:
            new_line += word + " "
    return new_line

def capitalize_line(line):
    line = re.sub(r'[^\w\s]', '', line) # remove punctuation
    line = line.upper() # capitalize
    return line

def get_stopw_list(stopw_f):
    stopwords = []
    for line in stopw_f.readlines():
        stopwords.append(line.upper().strip())
    return stopwords