import sys
import re

def main():
    for arg in sys.argv[1:]:
        regexp(arg)


def regexp(pathname):
    """Determines if the line of text in the file is an email through regular expressions."""

    # open file for reading
    f = open(pathname, 'r')

    # iterate through file lines
    for line in f.readlines():

        # set regular expression
        exp = re.compile(".@[a-z|A-Z|0-9][.]\\b[com|edu|gov|dev|net|co|co.uk|de|biz|me|info|org|us]\\b")

        print line

        if "Match" in str(exp.match(line)):
            print "true"
        else:
            print "false"
