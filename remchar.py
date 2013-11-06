import sys
import string

def remchar(pathname):
    """Remove characters from a substring from a string."""

    for line in open(pathname, 'r').readlines():
        # find letters to scrub and iterate through them and the strings
        splits = str(line).split(", ")
        scrubs = splits[1].split()
        for scrub in scrubs:
            for i in range(0,len(scrub)):
                splits[0] = splits[0].replace(scrub[i],"")
        print splits[0]

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        remchar(arg)
