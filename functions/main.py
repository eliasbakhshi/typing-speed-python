"""
functions the application
 """

import time
import random
import math


def clear_console():
    """ Clear the console """
    print(chr(27) + "[2J" + chr(27) + "[;H")


def sanitize_str(word, characters_to_remove=None):
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


def get_animal_name(score=0):
    """ Get the an animal name according to the score """
    animals = {
        1: "Sloths",
        2: "Snail",
        3: "Manatee",
        4: "Human",
        5: "Gazelle",
        6: "Ostrich",
        7: "Swordfish",
        8: "Spurred goose",
        9: "Pintail Sailfish",
        10: "Golden eagle",
        12: "Peregrine falcon"
    }
    score = score // 10
    return animals.get(score, None)


def start_practice(lines):
    """ Show lines and get info """
    failures = {}
    finish_time = 0
    count_written_words = 0
    count_extra_word = count_failed_words = count_total_words = count_total_character = 0
    start_time = time.time()
    # Go through each line and compare it with the input
    for line in lines:
        line = line.strip()
        clear_console()
        print(line)
        # Start timer
        the_input = input("")
        # Make list and count words and characters
        count_total_words += int(len(sanitize_str(line, ".").split(" ")))
        count_total_character += int(len(sanitize_str(the_input, ". \n")))
        line = sanitize_str(str(line), ".").strip().split(" ")
        the_input = sanitize_str(str(the_input), ".").strip().split(" ")
        # if the written line has more words, then save the amount of extra words.
        if len(the_input) > len(line):
            count_extra_word = len(the_input) - len(line)
        count_written_words += len(the_input)
        # If the written line has more words add extra empty parameters to the list
        if len(line) - len(the_input):
            the_input.extend([' '] * (len(line) - len(the_input)))
        # First make a list of words to compare word by word
        for key, value in enumerate(line):
            if value != the_input[key]:
                count_failed_words += 1
                # Take the word and compare it with the written word.
                for the_key, the_value in enumerate(value):
                    # Make sure that the second list has the same length
                    second_word = the_input[key].ljust(len(value))
                    if the_value != second_word[the_key]:
                        # Count and save the fail word
                        failures[the_value] = failures.get(the_value, 0) + 1

    finish_time = time.time()
    duration_sec = math.ceil((finish_time - start_time))
    gross_wpm = (count_written_words * 60) / duration_sec
    net_wpm = gross_wpm - ((count_failed_words * 60) / duration_sec)
    return {
        "failed_letters": sorted(failures.items(), key=lambda item: item[1], reverse=True),
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
    print("Failed letters:")
    print(result['failed_letters'])
    print("Percentage failure: " + str(result["percentage_failure"]) + "%")
    print("Total time: ", str(result['duration']))
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
        # Write to the end of the file.
        f_score.write(f"{next_line}{result['name']}|{result['net_wpm']}|{result['level']}")
        return True


def show_result_table(file_name):
    """ Show the result from the score.txt """
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
    return chr(random.randint(33, 126))


def practice_random_char():
    """ Get and display one random character."""
    # Initiate and save some info in the variables such as limited time
    duration_sec = int(input("How long do you want to play in seconds? "))
    start_time = time.time()
    count_failed_character = count_total_character = 0
    failures = {}
    # Show some random character and compare it with the user's input
    while duration_sec > time.time() - start_time:
        clear_console()
        random_char = str(get_random_char()).strip()
        print(random_char)
        the_input = input("").strip()
        count_total_character += 1
        # Compare and save if the characters do not match.
        if the_input != random_char:
            count_failed_character += 1
            failures[random_char] = failures.get(random_char, 0) + 1

    gross_wpm = (count_total_character * 60) / duration_sec
    net_wpm = gross_wpm - ((count_failed_character * 60) / duration_sec)

    return {
        "failed_letters": sorted(failures.items(), key=lambda item: item[1], reverse=True),
        "duration": duration_sec,
        "count_failed_character": count_failed_character,
        "count_total_character": count_total_character,
        "gross_wpm": gross_wpm,
        "net_wpm": net_wpm
    }
