pi_file = "./pi6.txt"


def get_digits():
    file_data = open(pi_file)
    pi = file_data.read()
    if file_data is None:
        raise FileEmptyException("Pi txt file is empty.")

    pi = pi.replace('\n', '')

    return pi[2:]  # the 3. at the start would cause problems, and we don't care about it


class FileEmptyException(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return "FileEmptyError: , {0}".format(self.message)
        else:
            return "FileEmptyError: The file you tried to open is empty."
