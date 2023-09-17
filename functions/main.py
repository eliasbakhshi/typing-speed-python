"""
functions the application
 """


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
    fails = None
    for line in lines:
        line = line.strip()
        print(line)
        the_input = str(input("")).strip()
        if the_input is not "":
        # Compare both lines at the same time and store the wrong characters
            for key, value in enumerate(line):
                if value is not the_input[key] and value is not "":
                    fails[the_input[key]] = fails.get(the_input[key], 0) + 1
    if fails is not None: return dict[sorted(fails.items(), key=lambda item: item[1], reverse=True)]
    else: return "You need to enter something to see the result."
