"""
This the main file for the application
"""

from functions.main import get_lines, get_text, show_lines, clearConsole, save_result, show_result, practice_random_char


def main():
    """ Script starts from here """
    is_running = True
    while is_running:
        # The menu
        clearConsole()
        print("--- <<< The menu >>> ---")
        print("\n")
        print("1:  Easy.")
        print("2:  Medium.")
        print("3:  Hard.")
        print("4:  Show Result.")
        print("5:  Practice character.")
        print("")
        print("q:  Quit.")
        print(2*"\n")

        u_choice = str(input("Your choice: "))
        if u_choice == "q":
            is_running = False
        elif u_choice == "1":
            the_lines = get_lines("typing/easy copy.txt")
            result = show_lines(the_lines)
            input("Press enter to see the result ...")
            clearConsole()
            present_fail = 100 - (((result['count_total_words'] - result['count_failed_words'] - result['count_extra_word'] ) / result['count_total_words']) * 100)
            print("Feltecken:")
            print(result['failed_letters'])
            print("Precentuellt fel: " + str(present_fail) + "%")
            print("Total tid: ", str(result['duration']))
            print("Gross WPM: ", result['gross_WPM'])
            print("Net WPM: ", result['net_WPM'])
            result["name"] = str(input("\nEnter username to add to high score: "))
            result["level"] = "easy"
            if save_result("typing/score.txt", result) : print("The information has been saved")
            else: print("Something went wrong!")




        elif u_choice == "2":
            print(get_lines("typing/medium.txt"))
            result = show_lines(the_lines)
            input("Press enter to see the result ...")
            print("Feltecken:")
            print(result)

        elif u_choice == "3":
            print(get_text("typing/hard.txt"))
            result = show_lines(the_lines)
            input("Press enter to see the result ...")
            print("Feltecken:")
            print(result)

        elif u_choice == "4":
            clearConsole()
            show_result("typing/score.txt")

        elif u_choice == "5":
            clearConsole()
            result = practice_random_char()
            present_fail = (result['count_failed_character'] / result['count_total_character']) * 100
            print("Feltecken:")
            print(result['failed_letters'])
            print("Precentuellt fel: " + str(present_fail) + "%")
            print("Gross WPM: ", result['gross_WPM'])
            print("Net WPM: ", result['net_WPM'])
        else:
            print("The choice is not in the menu.")

        if is_running:
            print(2*"\n")
            input(f"please press the enter to go back to the menu.")
            print(2*"\n")



if __name__ == "__main__":
    main()
