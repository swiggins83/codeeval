import string
import sys

def main():
    
    for arg in sys.argv[1:]:
        isSelfDesc(arg)


def isSelfDesc(pathname):
    """Determines if a number is self describing or not."""


    f = open(str(pathname), 'r')

    for s in f.readlines():

        for i in range(0,len(s)-1):
            if int(s[i]) is s.count(str(i)):
                if i is len(s)-2:
                    print '1'
            else:
                if i is len(s)-2:
                    print '0'

if __name__ == '__main__':
    main()
