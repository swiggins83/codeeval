import sys
import string


def main():

    for arg in sys.argv[1:]:
        rightmost(arg)


def rightmost(pathname):
    """Print position of character in a string."""

    f = open(str(pathname), 'r')

    for s in f.readlines():
        if len(s) > 0:
            res = s.split(",")

            result = res[0].rfind(res[1].split("\n")[0])

            print result

if __name__ == '__main__':
    main()
