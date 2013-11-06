import sys
import string

def rightmost(pathname):
    """Print position of character in a string."""

    for s in open(pathname, 'r').readlines():
        if len(s) > 0:
            res = s.split(",")

            print res[0].rfind(res[1].split("\n")[0])

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        rightmost(arg)
