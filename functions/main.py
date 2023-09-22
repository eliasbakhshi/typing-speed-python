"""
functions the application
 """

import time
import random
import math

def clear_console():
    """ Clear the console """
    print(chr(27) + "[2J" + chr(27) + "[;H")


def sanitize_str(word, characters_to_remove = None):
    """ Removes extra characters from the string """
    if characters_to_remove is not None and isinstance(characters_to_remove, str):
        for the_char in characters_to_remove:
            word = word.replace(the_char, "")
    return word

def get_lines(file_name):
    """ Get text file's content line by line """
    with open(file_name, encoding="utf-8") as f_easy:
        return f_easy.readlines()

def get_text(file_name):
    """ Get entire text file's content """
    with open(file_name, encoding="utf-8") as f_easy:
        return f_easy.read()


def get_animal_name(score = 0):
    """ Get the an animal name according to the score """
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

def start_practice(lines):
    """ Show lines and get info """
    fails = {}
    start_time = 0
    finish_time = 0
    count_written_words = 0
    count_extra_word = count_failed_words = count_total_words = count_total_character= 0
    start_time = time.time()
    for line in lines:
        line = line.strip()
        clear_console()
        print(line)
        # Start timer
        the_input = input("")
        count_total_words += int(len(sanitize_str(line,".,-()").split(" ")))
        count_total_character += int(len(sanitize_str(the_input,".,-() \n")))
        line = sanitize_str(str(line), ".,-()").strip().split(" ")
        the_input = sanitize_str(str(the_input), ".,-()").strip().split(" ")
        #if the written line has more words
        if len(the_input) > len(line):
            count_extra_word = len(the_input) - len(line)
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
    duration_sec =  math.ceil((finish_time - start_time))
    gross_wpm = (count_written_words * 60) / duration_sec
    net_wpm = gross_wpm - ((count_failed_words * 60) / duration_sec)
    return {
        "failed_letters": sorted(fails.items(), key=lambda item: item[1], reverse=True),
        "count_extra_word": count_extra_word,
        "count_failed_words": count_failed_words,
        "count_total_words": count_total_words,
        "count_total_character": count_total_character,
        "duration": str(round(duration_sec, 1)) + "s",
        "gross_wpm": gross_wpm,
        "net_wpm": net_wpm,
        "category": get_animal_name(net_wpm)
    }

def display_result(result):
    """ Display result information in the console. """
    clear_console()
    present_fail = 100 - ((((result['count_total_words'] -
                             result['count_failed_words'] - result['count_extra_word'] ) /
                             result['count_total_words']) * 100))
    print("Feltecken:")
    print(result['failed_letters'])
    print("Precentuellt fel: " + str(present_fail) + "%")
    print("Total tid: ", str(result['duration']))
    print("Gross WPM: ", result['gross_wpm'])
    print("Net WPM: ", result['net_wpm'])

def save_result(file_name, result):
    """ Save the result in the score.txt """
    with open(file_name, "a+", encoding="UTF-8") as f_score:
        # Check if the last line has next line character or not
        f_score.seek(0)
        the_content = f_score.read()
        next_line = ""
        if len(the_content):
            last_char = the_content[-1]
            if last_char != "\n":
                next_line = "\n"
        f_score.write(f"{next_line}{result['name']}|{result['net_wpm']}|{result['level']}")
        return True

def show_result(file_name):
    """ Show the result from the score.txt """
    levels = ["easy", "medium", "hard"]
    levels.sort(reverse=True)
    with open(file_name, encoding="UTF-8") as f_score:
        the_lines = f_score.readlines()
        the_list = []
        for the_line in the_lines:
            the_list.append(the_line.strip().split("|"))
        # Order by score
        the_list.sort(key=lambda row: row[1], reverse=True)
        # Order by level
        the_list.sort(key=lambda row: row[2], reverse=True)
        for the_line in the_list:
            # Print line in the format
            print(f"{the_line[0]: <20} {the_line[1]: <20} {the_line[2]: <20}")

def get_random_char():
    """ Generate a random character. """
    random_num = random.randint(33,126)
    return chr(random_num)

def practice_random_char():
    """ Get and display one random character."""
    # Get limited time that user want to play
    duration_sec = int(input("How long do you want to play in seconds? "))
    start_time = time.time()
    count_failed_character = count_total_character = 0
    fails = {}

    while duration_sec > time.time() - start_time :
        clear_console()
        random_char = str(get_random_char()).strip()
        print(random_char)
        the_input = input("").strip()
        count_total_character += 1
        if the_input != random_char:
            count_failed_character += 1
            fails[random_char] = fails.get(random_char, 0) + 1

    gross_wpm = (count_total_character * 60) / duration_sec
    net_wpm = gross_wpm - ((count_failed_character * 60) / duration_sec)

    return {
        "failed_letters": sorted(fails.items(), key=lambda item: item[1], reverse=True),
        "count_failed_character": count_failed_character,
        "count_total_character": count_total_character,
        "gross_wpm": gross_wpm,
        "net_wpm": net_wpm
    }
