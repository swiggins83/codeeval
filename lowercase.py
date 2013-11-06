import sys
import string

def main():
    for arg in sys.argv[1:]:
        f = open(arg,'r')
        for line in f.readlines():
            print line.lower()

if __name__ == "__main__":
    main()
