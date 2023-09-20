"""
functions the application
 """

import os
import time

def clearConsole():
    """ Clear the console """
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def sanitize_str(word, characters_to_remove = None):
    """ Removes extra characters from the string """
    if characters_to_remove is not None and isinstance(characters_to_remove, str):
        for the_char in characters_to_remove:
            word = word.replace(the_char, "")
    return word

def get_lines(file_name):
    """ Get text file's content line by line """
    with open(file_name) as f_easy:
        return f_easy.readlines()

def get_text(file_name):
    """ Get entire text file's content """
    with open(file_name) as f_easy:
        return f_easy.read()


def get_animal_name(score = 0):
    if 10 <= score < 20:
        return "Sengångare"
    elif 20 <= score < 30:
        return "Snigel"
    elif 30 <= score < 40:
        return "Sjöko"
    elif 40 <= score < 50:
        return "Människa"
    elif 50 <= score < 60:
        return "Gasell"
    elif 60 <= score < 70:
        return "Struts"
    elif 70 <= score < 80:
        return "Svärdfisk"
    elif 80 <= score < 90:
        return "Sporrgås"
    elif 90 <= score < 100:
        return "Taggstjärtseglare"
    elif 100 <= score < 120:
        return "Kungsörn"
    elif 120 <= score:
        return "Pilgrimsfalk"
    return None

def show_lines(lines):
    """ Show lines and get info """
    fails = {}
    start_time = 0
    finish_time = 0
    count_written_words = 0
    for line in lines:
        count_extra_word = count_failed_words = count_total_words = count_total_character= 0
        count_total_words += int(len(sanitize_str(line,".,-()").split(" ")))
        count_total_character += int(len(sanitize_str(line,".,-() \n")))
        line = line.strip()
        clearConsole()
        print(line)
        # Start timer
        start_time = time.time()
        the_input = sanitize_str(str(input("")), ".,-()").strip().split(" ")
        line = sanitize_str(str(line), ".,-()").strip().split(" ")
        #if the written line has more words
        if len(the_input) > len(line): count_extra_word = len(the_input) - len(line)
        count_written_words += len(the_input)
        #if the written line has more words add extra empty parameters to the list
        if len(line) - len(the_input):
            the_input.extend([' '] * (len(line) - len(the_input)))
        # First make a list of words to compare word by word
        for key, value in enumerate(line):
            if value != the_input[key]:
                count_failed_words += 1
                # Take the word and compare it with the given word.
                for the_key, the_value in enumerate(value):
                    second_word = the_input[key].ljust(len(value))
                    if the_value != second_word[the_key]:
                        fails[the_value] = fails.get(the_value, 0) + 1

    finish_time = time.time()
    duration_min = round((finish_time - start_time) / 60)
    if duration_min < 1: duration_min = 1
    return {
        "failed_letters": sorted(fails.items(), key=lambda item: item[1], reverse=True),
        "count_extra_word": count_extra_word,
        "count_failed_words": count_failed_words,
        "count_total_words": count_total_words,
        "count_total_character": count_total_character,
        "duration": finish_time - start_time,
        "gross_WPM": count_written_words / duration_min,
        "net_WPM": (count_written_words / duration_min) - (count_failed_words / duration_min),
        "category": get_animal_name(int((count_written_words / duration_min) - (count_failed_words / duration_min)))
    }
