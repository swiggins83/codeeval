import sys
import string

def armstrong(pathname):
    """Determines if a number is an armstrong number."""

    for s in open(pathname, 'r').readlines():

        summ = 0
        for i in range(0,len(s)-1):
            summ += int(s[i])**(len(s)-1)

        if summ is not int(s):
            print False
        else:
            print True


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        armstrong(arg)
