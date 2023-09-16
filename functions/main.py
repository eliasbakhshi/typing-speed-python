"""
functions the application
 """


def get_lines(file_name):
        with open(file_name) as f_easy:
            return f_easy.readlines()

def get_text(file_name):
    with open(file_name) as f_easy:
        return f_easy.read()
