import sys

def reversewords(pathname):
    """Reverse two words separated by a whitespace."""

    for line in open(pathname, 'r').readlines():
        if len(line) > 0:
            split = line.split("\n")[0].split(" ")
            print split[1] + " " + split[0]

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        reversewords(arg)
