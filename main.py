"""
This the main file for the application
"""

import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
#pylint: disable=wrong-import-position
from functions.main import get_lines, get_text, show_lines
#pylint: enable=wrong-import-position


def main():
    """ Script starts from here """
    is_running = True
    while is_running:
        # The menu
        print(2*"\n")
        print("--- <<< The menu >>> ---")
        print("\n")
        print("1:  Easy.")
        print("2:  Medium.")
        print("3:  Hard.")
        print("q:  Quit.")
        print(2*"\n")

        u_choice = str(input("Your choice: "))
        if u_choice == "q":
            is_running = False
        elif u_choice == "1":
            the_lines = get_lines("typing/easy copy.txt")
            result = show_lines(the_lines)
            input("Press enter to see the result ...")
            print("Feltecken:")
            print(result)

        elif u_choice == "2":
            print(get_lines("typing/medium.txt"))

        elif u_choice == "3":
            print(get_text("typing/hard.txt"))

        else:
            print("The choice is not in the menu.")

        if is_running:
            print(2*"\n")
            input(f"please press the enter to go back to the menu.")
            print(2*"\n")



if __name__ == "__main__":
    main()
