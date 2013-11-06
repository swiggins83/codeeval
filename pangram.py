import sys
import string

def main():
    for arg in sys.argv[1:]:
        pangram(arg)


def pangram(pathname):

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    f = open(pathname,'r')

    for line in f.readlines():
        missing = []
        for letter in letters:
            if letter not in line.lower():
                missing.append(letter)
        if len(missing)>0:
            for miss in missing:
                sys.stdout.write(miss)
        else:
            sys.stdout.write('NULL')
        print

if __name__ == "__main__":
    main()
