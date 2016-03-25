#! python
"""
Module that runs pylint on all python scripts found in a directory tree..

**NOTE**: The pylint executable script must be on the PATH.

"""

import os
import re
import argparse

total = 0.0
count = 0


def __print_header__():
    print("==" * 37)
    print("|" + "\t" * 9 + " |")
    print("|" + "\t\t\tVERIFYING CODE COVERAGE " + "\t" * 3 + " |")
    print("|" + "\t\t\t(using pylint tool) " + "\t" * 4 + " |")
    print("|" + "\t" * 9 + " |")
    print("==" * 37)


def __print_footer__():
    print("==" * 37)
    print("|" + "\t" * 9 + " |")
    if count:
        print("|" + "\t\t\t%d module(s) found" % count + "\t" * 4 + " |")
        print("|" + "\t\t\tAVERAGE SCORE = %.02f" % (total / count) + "\t" * 4 + " |")
    else:
        print("\t\t\tNo modules found! -> make sure you have pylint on your PATH!")
    print("|" + "\t" * 9 + " |")
    print("==" * 37)


def __check__(l_root, l_name, l_path):
    """
    apply pylint to the file specified if it is a *.py file
    :param l_root: folder path
    :param l_name: file name
    :param l_path:  folder + file (path)
    """
    global total, count
    # handle the case when argument has local path
    if len(l_root) == 0:
        l_root = os.getcwd()
    if l_path.endswith('.py'):
        command = "pylint %s" % l_path
        pout = os.popen(command, 'r')
        for line in pout:
            if re.match("E....:.", line):
                print(line)
            if "Your code has been rated at" in line:
                print(line)
                score = re.findall("\d+.\d\d", line)[0]
                total += float(score)
                count += 1
                command = "pylint -f html " + l_path + " > " + l_root \
                          + "\\htmlcov\\" + l_name[:-3] + ".html   "
                os.popen(command, 'r')
                return


def __create_htmlcov__(file_path):
    # create htmlcov coverage folder if non-existent
    htmlcov_path = os.path.join(file_path, "htmlcov")
    try:
        os.stat(htmlcov_path)
    except OSError:
        os.mkdir(htmlcov_path)


def __check_dir__(dir_path):
    for root, dirs, files in os.walk(dir_path):
        for name in files:
            path = os.path.join(root, name)
            if name.endswith('.py'):
                print("\n--> CHECKING file: " + name + "\n")
                __check__(root, name, path)


def __check_file__(file_path):
    path = file_path
    root = os.path.dirname(file_path)
    name = os.path.basename(file_path)
    __check__(root, name, path)


def __arguments__():
    parser = argparse.ArgumentParser(description='Pylint Code Verifier.')
    parser.add_argument('file', help='Please provide the file/directory '
                                     '(leave empty for current directory).', nargs='*')
    return parser.parse_args().file


if __name__ == "__main__":
    arguments = __arguments__()
    __print_header__()
    if len(arguments) == 0:
        print("\n**ALERT**: No argument specified -> using local directory\n")
        __create_htmlcov__(os.getcwd())
        __check_dir__(os.getcwd())
    for arg in arguments:
        if arg.endswith('.py'):
            print("\nCHECKING single file: " + os.path.basename(arg) + "\n")
            __create_htmlcov__(os.path.dirname(arg))
            __check_file__(arg)
        else:
            print("\nCHECKING all *.py scripts in subdirectories of: ", arg)
            __create_htmlcov__(arg)
            __check_dir__(arg)
    __print_footer__()
