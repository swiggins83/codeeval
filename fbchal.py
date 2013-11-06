import string
import operator
import sys

def findBeauty(pathname):
    """Find the maximum beauty of strings from a file."""

    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for s in open(pathname, 'r').readlines():

        lettercount = {}
        beauty = {}

        s = s.lower()

        for letter in s:
            if letter in letters:
                lettercount[letter] = s.count(letter)

        j = 0
        while len(lettercount) != 0:
            beauty[max(lettercount.iteritems(), key=operator.itemgetter(1))[0]] = 26-j
            lettercount.pop(max(lettercount.iteritems(), key=operator.itemgetter(1))[0])
            j += 1

        summ = 0
        for i in range(0,len(beauty)):
            summ += beauty.values()[i] * s.count(beauty.keys()[i])

        print summ
        beauty.clear()


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        findBeauty(arg)
