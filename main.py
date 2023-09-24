"""
This the main file for the application
"""

import functions.main as mf


def main():
    """ Script starts from here """
    is_running = True
    while is_running:
        # The menu
        mf.clear_console()
        print("--- <<< The menu >>> ---")
        print(("""

1:  Easy.
2:  Medium.
3:  Hard.
4:  Show Result.
5:  Practice Character.

q:  Quit.


"""))
        u_choice = str(input("Your choice: "))
        if u_choice == "q":
            is_running = False
        elif u_choice == "1":
            the_lines = mf.get_lines("typing/easy.txt")
            result = mf.start_practice(the_lines)
            input("Press enter to see the result ...")
            result["percentage_failure"] = 100 - ((((result['count_total_words'] -
                                                     result['count_failed_words'] -
                                                     result['count_extra_word']) /
                                                    result['count_total_words']) * 100))
            mf.display_result(result)
            result["name"] = str(input("\nEnter username to add to high score: "))
            result["level"] = "easy"
            if mf.save_result("typing/score.txt", result):
                print("The information has been saved")
            else:
                print("Something went wrong!")

        elif u_choice == "2":
            the_lines = mf.get_lines("typing/medium.txt")
            result = mf.start_practice(the_lines)
            input("Press enter to see the result ...")
            result["percentage_failure"] = 100 - ((((result['count_total_words'] -
                                                     result['count_failed_words'] -
                                                     result['count_extra_word']) /
                                                    result['count_total_words']) * 100))
            mf.display_result(result)
            result["name"] = str(input("\nEnter username to add to high score: "))
            result["level"] = "medium"
            if mf.save_result("typing/score.txt", result):
                print("The information has been saved")
            else:
                print("Something went wrong!")

        elif u_choice == "3":
            the_lines = mf.get_lines("typing/hard.txt")
            result = mf.start_practice(the_lines)
            input("Press enter to see the result ...")
            result["percentage_failure"] = 100 - ((((result['count_total_words'] -
                                                     result['count_failed_words'] -
                                                     result['count_extra_word']) /
                                                    result['count_total_words']) * 100))
            mf.display_result(result)
            result["name"] = str(input("\nEnter username to add to high score: "))
            result["level"] = "hard"
            if mf.save_result("typing/score.txt", result):
                print("The information has been saved")
            else:
                print("Something went wrong!")

        elif u_choice == "4":
            mf.clear_console()
            try:
                mf.show_result_table("typing/score.txt")
            except FileNotFoundError:
                print("There is not any score to show.")

        elif u_choice == "5":
            try:
                mf.clear_console()
                result = mf.practice_random_char()
                result["percentage_failure"] = ((result['count_failed_character'] /
                                                result['count_total_character']) * 100)
                mf.display_result(result)
            except ValueError:
                print("You need to write the write value.")
        else:
            print("The choice is not in the menu.")

        if is_running:
            print(2*"\n")
            input("please press the enter to go back to the menu.")
            print(2*"\n")


if __name__ == "__main__":
    main()
