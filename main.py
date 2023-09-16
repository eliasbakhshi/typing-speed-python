"""
This the main file for the application
 """
import os


def get_path(relative_path):
    script_dir = os.path.dirname(__file__)
    return os.path.join(script_dir, relative_path)
the_path = get_path("../functions.py")
from ..typing import functions

functions.test2()
print("test")
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '../typing/easy.txt')
with open(get_path("../typing/easy.txt")) as htest:
    print(htest.read())

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
        print("word_frequency :  Word frequency.")
        print("q:  Quit.")
        print(3*"\n")

        u_choice = str(input("Your choice: "))
        if u_choice == "q":
            is_running = False
        elif u_choice == "1":
            print(f.easy_line(get_path("../typing/easy.txt")))
            pass

        elif u_choice == "2":
            # print(f.easy_line("easy.txt"))
            pass

        elif u_choice == "3":
            # print(f.easy_line("easy.txt"))
            pass

        else:
            print("The choice is not in the menu.")

        if is_running:
            input("please press the enter to go to menu.")
            print(3*"\n")



if __name__ == "__main__":
    main()
