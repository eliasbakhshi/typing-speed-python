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

def show_lines(lines):
    """ Show lines and get info """
    fails = {}
    start_time = 0
    finish_time = 0
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
        if len(the_input) > len(line): count_extra_word = len(the_input) - len(line)
        print(line)
        print(the_input)
        # Make sure that the_input has at lease the same length as the line list
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
    return {
        "failed_letters": sorted(fails.items(), key=lambda item: item[1], reverse=True),
        "count_extra_word": count_extra_word,
        "count_failed_words": count_failed_words,
        "count_total_words": count_total_words,
        "count_total_character": count_total_character,
        "duration": finish_time - start_time

    }
