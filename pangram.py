import sys
import string

def pangram(pathname):

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for line in open(pathname, 'r').readlines():
        missing = []
        for letter in letters:
            if letter not in line.lower():
                missing.append(letter)
        if len(missing) > 0:
            for miss in missing:
                sys.stdout.write(miss)
        else:
            sys.stdout.write('NULL')
        print

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        pangram(arg)
